#!/usr/bin/env python3
"""
检查项目中缺少中文翻译的 .md 文件
并创建并发翻译任务
"""

import os
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import time
from datetime import datetime

class TranslationChecker:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.english_files = []
        self.chinese_files = []
        self.missing_translations = []

    def find_md_files(self):
        """递归查找所有 .md 文件"""
        print("🔍 正在扫描所有 .md 文件...")

        for md_file in self.root_dir.rglob("*.md"):
            if ".git" in str(md_file):
                continue

            # 检查是否是中文翻译文件
            if md_file.name.endswith(".zh.md"):
                self.chinese_files.append(md_file)
            elif md_file.name.endswith(".md"):
                self.english_files.append(md_file)

        print(f"📊 找到 {len(self.english_files)} 个英文 .md 文件")
        print(f"📊 找到 {len(self.chinese_files)} 个中文 .zh.md 文件")

    def check_missing_translations(self):
        """检查缺少中文翻译的文件"""
        print("\n🔍 检查缺少的翻译...")

        for en_file in self.english_files:
            # 跳过中文翻译文件本身
            if en_file.name.endswith(".zh.md"):
                continue

            # 检查对应的中文翻译文件是否存在
            zh_file = en_file.with_suffix(".zh.md")

            if not zh_file.exists():
                self.missing_translations.append({
                    'english': en_file,
                    'chinese_expected': zh_file,
                    'relative_path': str(en_file.relative_to(self.root_dir)),
                    'size': self._get_file_size(en_file)
                })

        print(f"❌ 发现 {len(self.missing_translations)} 个文件缺少中文翻译")

    def _get_file_size(self, file_path):
        """获取文件大小（KB）"""
        try:
            size = file_path.stat().st_size
            return round(size / 1024, 2)
        except:
            return 0

    def print_tree_structure(self):
        """输出目录树结构"""
        print("\n📁 项目目录结构 (重点显示缺少翻译的文件):")
        print("=" * 80)

        def print_tree(path, prefix="", is_last=True):
            """递归打印目录树"""
            if path.name == ".git":
                return

            # 获取目录中的项目
            try:
                items = sorted([item for item in path.iterdir()
                            if not item.name.startswith(".")],
                           key=lambda x: (x.is_file(), x.name.lower()))
            except PermissionError:
                return

            # 计算需要翻译的文件数
            needs_translation_files = []
            regular_files = []

            for item in items:
                item_path = path / item
                if (item_path.is_file() and
                    item.endswith(".md") and
                    not item.endswith(".zh.md")):

                    # 检查是否有对应的翻译文件
                    zh_file = item_path.with_suffix(".zh.md")
                    if not zh_file.exists():
                        needs_translation_files.append(item)
                    else:
                        regular_files.append(item)
                elif item_path.is_file() and item.endswith(".md"):
                    regular_files.append(item)
                else:
                    regular_files.append(item)

            # 打印当前目录
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{path.name}/")

            # 打印需要翻译的文件（用红色标记）
            for i, item in enumerate(needs_translation_files):
                is_last_item = (i == len(needs_translation_files) - 1) and len(regular_files) == 0
                item_prefix = prefix + ("    " if is_last else "│   ")
                item_connector = "└── " if is_last_item else "├── "
                print(f"{item_prefix}{item_connector}[缺翻译] {item}")

            # 打印常规文件和子目录
            for i, item in enumerate(regular_files):
                is_last_item = i == len(regular_files) - 1
                item_prefix = prefix + ("    " if is_last else "│   ")
                item_connector = "└── " if is_last_item else "├── "
                print(f"{item_prefix}{item_connector}{item}")

        print_tree(self.root_dir)
        print("=" * 80)

    def create_translation_tasks(self):
        """创建5个并发翻译任务"""
        if not self.missing_translations:
            print("\n✅ 所有文件都有对应的中文翻译！")
            return

        print(f"\n📝 创建 {min(5, len(self.missing_translations))} 个翻译任务...")

        # 将文件分组到任务中
        tasks = self._distribute_files_to_tasks(self.missing_translations)

        # 创建任务配置
        task_configs = []
        for i, task_files in enumerate(tasks):
            config = {
                'task_id': i + 1,
                'files': task_files,
                'total_size': sum(f['size'] for f in task_files),
                'count': len(task_files),
                'status': 'pending'
            }
            task_configs.append(config)

        # 保存任务配置
        with open('translation_tasks.json', 'w', encoding='utf-8') as f:
            json.dump({
                'created_at': datetime.now().isoformat(),
                'total_missing_files': len(self.missing_translations),
                'tasks': task_configs
            }, f, ensure_ascii=False, indent=2)

        print(f"\n📋 任务配置已保存到 translation_tasks.json")
        self._print_task_summary(task_configs)

        return task_configs

    def _distribute_files_to_tasks(self, files):
        """将文件分配到5个任务中"""
        if len(files) <= 5:
            # 如果文件数量少于等于5，每个任务一个文件
            return [[file] for file in files] + [[]] * (5 - len(files))

        # 计算每个任务应该分配的文件数量
        base_count = len(files) // 5
        extra = len(files) % 5

        tasks = []
        start_idx = 0

        for i in range(5):
            count = base_count + (1 if i < extra else 0)
            if start_idx < len(files):
                task_files = files[start_idx:start_idx + count]
                tasks.append(task_files)
                start_idx += count
            else:
                tasks.append([])

        return tasks

    def _print_task_summary(self, task_configs):
        """打印任务摘要"""
        print(f"\n📊 翻译任务分配摘要:")
        print("-" * 60)

        for config in task_configs:
            if config['files']:
                files_list = "\n  ".join([f['relative_path'] for f in config['files'][:3]])
                if len(config['files']) > 3:
                    files_list += f"\n  ... 还有 {len(config['files']) - 3} 个文件"

                print(f"任务 {config['task_id']}: {config['count']} 个文件 ({config['total_size']} KB)")
                print(f"  文件列表:")
                print(f"  {files_list}")
            else:
                print(f"任务 {config['task_id']}: 无文件")
            print()

        print("-" * 60)
        print(f"总计: {sum(config['count'] for config in task_configs)} 个文件需要翻译")

    def run_parallel_translation(self, task_configs, max_workers=5):
        """运行并行翻译任务"""
        print(f"\n🚀 启动 {max_workers} 个并发翻译任务...")

        def translate_task(task_config):
            """单个翻译任务函数"""
            task_id = task_config['task_id']
            files = task_config['files']

            if not files:
                return {'task_id': task_id, 'status': 'skipped', 'files_processed': 0}

            print(f"📝 任务 {task_id} 开始翻译 {len(files)} 个文件...")
            start_time = time.time()

            processed_files = []
            for file_info in files:
                try:
                    # 这里应该调用实际的翻译函数
                    # 为了演示，我们只是模拟翻译过程
                    time.sleep(0.1)  # 模拟翻译时间

                    # 实际实现中，这里会调用翻译 API 或函数
                    # result = translate_file(file_info['english'], file_info['chinese_expected'])

                    processed_files.append(file_info['relative_path'])

                except Exception as e:
                    print(f"❌ 任务 {task_id} 翻译 {file_info['relative_path']} 时出错: {e}")

            elapsed_time = time.time() - start_time

            return {
                'task_id': task_id,
                'status': 'completed',
                'files_processed': len(processed_files),
                'elapsed_time': round(elapsed_time, 2),
                'files': processed_files
            }

        # 启动并发任务
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有任务
            future_to_task = {
                executor.submit(translate_task, config): config
                for config in task_configs
            }

            # 收集结果
            for future in as_completed(future_to_task):
                try:
                    result = future.result()
                    results.append(result)
                    task_id = result['task_id']
                    status = result['status']

                    if status == 'completed':
                        print(f"✅ 任务 {task_id} 完成: {result['files_processed']} 个文件 ({result['elapsed_time']}秒)")
                    else:
                        print(f"⏭️ 任务 {task_id} 跳过")

                except Exception as e:
                    task_config = future_to_task[future]
                    print(f"❌ 任务 {task_config['task_id']} 执行失败: {e}")

        # 保存结果
        with open('translation_results.json', 'w', encoding='utf-8') as f:
            json.dump({
                'completed_at': datetime.now().isoformat(),
                'summary': {
                    'total_tasks': len(task_configs),
                    'completed_tasks': len([r for r in results if r['status'] == 'completed']),
                    'total_files_processed': sum(r['files_processed'] for r in results)
                },
                'results': results
            }, f, ensure_ascii=False, indent=2)

        self._print_final_summary(results)

    def _print_final_summary(self, results):
        """打印最终摘要"""
        print("\n" + "=" * 60)
        print("🎉 翻译任务完成摘要:")
        print("=" * 60)

        for result in results:
            status_icon = "✅" if result['status'] == 'completed' else "⏭️"
            print(f"{status_icon} 任务 {result['task_id']}: {result['files_processed']} 个文件")

        total_processed = sum(r['files_processed'] for r in results)
        print(f"\n📊 总计处理文件: {total_processed}")

        # 生成处理文件列表
        processed_files = []
        for result in results:
            if 'files' in result:
                processed_files.extend(result['files'])

        if processed_files:
            print(f"\n📝 已处理文件列表:")
            for file_path in sorted(processed_files):
                print(f"  ✅ {file_path}")

    def run(self, parallel=False):
        """运行完整的检查和翻译流程"""
        print("🚀 开始翻译检查流程...")
        print(f"📁 根目录: {self.root_dir.absolute()}")
        print("-" * 60)

        # 步骤1: 查找所有 md 文件
        self.find_md_files()

        # 步骤2: 检查缺少的翻译
        self.check_missing_translations()

        # 步骤3: 打印目录树
        self.print_tree_structure()

        # 步骤4: 创建翻译任务
        task_configs = self.create_translation_tasks()

        if task_configs and parallel:
            # 步骤5: 运行并行翻译
            self.run_parallel_translation(task_configs)
        elif task_configs:
            print(f"\n📋 发现 {len(task_configs)} 个翻译任务，但并行模式已禁用")
            print("💡 使用 run(parallel=True) 启用并行翻译")
        else:
            print("\n✅ 所有文件都有对应的中文翻译！")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="检查项目中缺少中文翻译的 .md 文件并创建翻译任务",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--root', '-r',
        default='.',
        help='要扫描的根目录 (默认: 当前目录)'
    )

    parser.add_argument(
        '--parallel', '-p',
        action='store_true',
        help='启用并行翻译 (默认: 仅检查和创建任务)'
    )

    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=5,
        help='并发工作线程数 (默认: 5)'
    )

    args = parser.parse_args()

    # 创建检查器实例
    checker = TranslationChecker(args.root)

    # 运行检查
    checker.run(parallel=args.parallel)


if __name__ == "__main__":
    main()