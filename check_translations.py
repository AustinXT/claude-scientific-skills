#!/usr/bin/env python3
"""
检查项目中缺少中文翻译的 .md 文件并输出树结构
"""

import os
from pathlib import Path
import json
from datetime import datetime

class TranslationChecker:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.english_files = []
        self.chinese_files = []
        self.missing_translations = []
        self.excluded_patterns = [
            '.git', 'node_modules', '__pycache__', '.pytest_cache',
            'venv', 'env', 'site-packages'
        ]

    def is_excluded(self, path):
        """检查路径是否应该被排除"""
        path_str = str(path)
        for pattern in self.excluded_patterns:
            if pattern in path_str:
                return True
        return False

    def find_md_files(self):
        """递归查找所有 .md 文件"""
        print("🔍 正在扫描所有 .md 文件...")

        for md_file in self.root_dir.rglob("*.md"):
            if self.is_excluded(md_file):
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
            relative_path = str(en_file.relative_to(self.root_dir))

            # 排除一些不需要翻译的文件
            if any(exclude in relative_path for exclude in [
                'LICENSE.md',
                'LICENSE.zh.md',  # 已存在的翻译
                'README.md',  # 已存在的翻译
                'README.zh.md',  # 已存在的翻译
                'docs/examples.md',  # 已存在的翻译
                'docs/examples.zh.md',  # 已存在的翻译
                'docs/scientific-skills.md',  # 已存在的翻译
                'docs/scientific-skills.zh.md',  # 已存在的翻译
            ]):
                continue

            if not zh_file.exists():
                self.missing_translations.append({
                    'english': en_file,
                    'chinese_expected': zh_file,
                    'relative_path': relative_path,
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

    def create_translation_tasks(self):
        """创建5个并发翻译任务"""
        if not self.missing_translations:
            print("\n✅ 所有文件都有对应的中文翻译！")
            return []

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

        print(f"📋 任务配置已保存到 translation_tasks.json")
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

    def print_tree_structure(self):
        """输出目录树结构（仅显示缺少翻译的文件）"""
        print("\n🌳 项目目录结构（缺少翻译的文件）:")
        print("=" * 80)

        # 按目录分组
        dir_structure = {}
        for item in self.missing_translations:
            path_parts = Path(item['relative_path']).parts
            if len(path_parts) > 1:
                dir_path = "/".join(path_parts[:-1])
                if dir_path not in dir_structure:
                    dir_structure[dir_path] = []
                dir_structure[dir_path].append(item)
            else:
                if 'root' not in dir_structure:
                    dir_structure['root'] = []
                dir_structure['root'].append(item)

        # 打印树结构
        def print_tree(path_dict, prefix="", is_last=True):
            items = list(path_dict.items())

            for i, (dir_path, files) in enumerate(sorted(items)):
                is_last_dir = i == len(items) - 1
                dir_name = dir_path.split('/')[-1] if '/' in dir_path else dir_path

                if dir_path == 'root':
                    connector = "" if is_last else "├── "
                else:
                    connector = "└── " if is_last else "├── "

                print(f"{prefix}{connector}📁 {dir_name}/")

                # 打印该目录下的文件
                for j, file_info in enumerate(sorted(files, key=lambda x: x['relative_path'])):
                    is_last_file = j == len(files) - 1
                    file_connector = "    └── " if is_last_file else "    ├── "
                    file_size = file_info['size']
                    size_indicator = ""
                    if file_size > 100:
                        size_indicator = " 📄"
                    elif file_size > 50:
                        size_indicator = " 📃"
                    else:
                        size_indicator = " 📄"

                    print(f"{prefix}{'│   ' if not is_last_dir else '    '}{file_connector}[缺翻译] {file_info['english'].name}{size_indicator} ({file_size}KB)")

        print_tree(dir_structure)

        print("=" * 80)

    def run(self):
        """运行完整的检查流程"""
        print("🚀 开始翻译检查流程...")
        print(f"📁 根目录: {self.root_dir.absolute()}")
        print("-" * 60)

        # 步骤1: 查找所有 .md 文件
        self.find_md_files()

        # 步骤2: 检查缺少的翻译
        self.check_missing_translations()

        # 步骤3: 打印目录树
        self.print_tree_structure()

        # 步骤4: 创建翻译任务
        task_configs = self.create_translation_tasks()

        return task_configs


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

    args = parser.parse_args()

    # 创建检查器实例
    checker = TranslationChecker(args.root)

    # 运行检查
    task_configs = checker.run()

    if task_configs:
        print(f"\n🎯 发现 {len(task_configs)} 个翻译任务")
        print("💡 提示: 可以使用以下命令并行处理这些任务:")
        print("   python -m concurrent.futures process_tasks")
        print("   或手动分配给不同的翻译人员处理")

    return task_configs


if __name__ == "__main__":
    main()