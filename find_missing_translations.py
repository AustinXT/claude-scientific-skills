#!/usr/bin/env python3
"""
查找项目中缺少中文翻译的 .md 文件并创建5个并发翻译任务
简单版本 - 不依赖外部库
"""

import os
import json
from pathlib import Path
from datetime import datetime

def find_missing_translations(root_dir="."):
    """查找缺少中文翻译的文件"""
    print("🔍 正在扫描所有 .md 文件...")

    english_files = []
    chinese_files = []
    missing_translations = []

    # 排除的文件
    excluded_files = {
        'LICENSE.md',
        'README.md',
        'docs/examples.md',
        'docs/scientific-skills.md',
        'CLAUDE.md'
    }

    # 递归查找所有 .md 文件
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file

                # 排除 .git 等目录
                if '.git' in str(file_path):
                    continue

                if file.endswith('.zh.md'):
                    chinese_files.append(file_path)
                elif file.endswith('.md'):
                    english_files.append(file_path)

    print(f"📊 找到 {len(english_files)} 个英文 .md 文件")
    print(f"📊 找到 {len(chinese_files)} 个中文 .zh.md 文件")

    # 检查缺少的翻译
    for en_file in english_files:
        # 跳过中文翻译文件和已排除的文件
        if (en_file.name.endswith('.zh.md') or
            en_file.name in excluded_files or
            'node_modules' in str(en_file) or
            '__pycache__' in str(en_file)):
            continue

        relative_path = str(en_file.relative_to(root_dir))

        # 检查对应的中文翻译文件是否存在
        zh_file = en_file.with_suffix('.zh.md')

        if not zh_file.exists():
            missing_translations.append({
                'english': en_file,
                'chinese_expected': zh_file,
                'relative_path': relative_path
            })

    print(f"❌ 发现 {len(missing_translations)} 个文件缺少中文翻译")
    return missing_translations

def create_translation_tasks(missing_files):
    """创建5个并发翻译任务"""
    if not missing_files:
        print("\n✅ 所有文件都有对应的中文翻译！")
        return []

    print(f"\n📝 创建 {min(5, len(missing_files))} 个翻译任务...")

    # 简单分配：前5个文件各一个任务，其余的分配到各个任务
    tasks = []
    for i in range(5):
        if i < len(missing_files):
            tasks.append([missing_files[i]])
        else:
            tasks.append([])

    # 如果还有更多文件，分配到各任务
    if len(missing_files) > 5:
        remaining_files = missing_files[5:]
        for i, extra_file in enumerate(remaining_files):
            tasks[i % 5].append(extra_file)

    # 创建任务配置
    task_configs = []
    for i, task_files in enumerate(tasks):
        config = {
            'task_id': i + 1,
            'files': task_files,
            'count': len(task_files),
            'status': 'pending'
        }
        task_configs.append(config)

    # 保存任务配置
    with open('translation_tasks.json', 'w', encoding='utf-8') as f:
        json.dump({
            'created_at': datetime.now().isoformat(),
            'total_missing_files': len(missing_files),
            'tasks': task_configs
        }, f, indent=2, ensure_ascii=False)

    print(f"📋 任务配置已保存到 translation_tasks.json")
    print_task_summary(task_configs)

    return task_configs

def print_task_summary(task_configs):
    """打印任务摘要"""
    print(f"\n📊 翻译任务分配摘要:")
    print("-" * 60)

    for config in task_configs:
        if config['files']:
            files_list = "\n  ".join([f['relative_path'] for f in config['files'][:5]])
            if len(config['files']) > 5:
                files_list += f"\n  ... 还有 {len(config['files']) - 5} 个文件"

            print(f"任务 {config['task_id']}: {config['count']} 个文件")
            print(f"  文件列表:")
            print(f"  {files_list}")
        else:
            print(f"任务 {config['task_id']}: 无文件")
        print()

    print("-" * 60)
    total_files = sum(config['count'] for config in task_configs)
    print(f"总计: {total_files} 个文件需要翻译")

def print_tree_structure(missing_files):
    """输出目录树结构（仅显示缺少翻译的文件）"""
    if not missing_files:
        return

    print("\n🌳 项目目录结构（缺少翻译的文件）:")
    print("=" * 80)

    # 按目录分组
    dir_structure = {}
    for item in missing_files:
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
    def print_tree(items, prefix=""):
        sorted_items = sorted(items, key=lambda x: x['relative_path'])

        for i, item in enumerate(sorted_items):
            is_last = i == len(sorted_items) - 1
            connector = "└── " if is_last else "├── "

            file_size = ""
            try:
                size = item['english'].stat().st_size
                size_kb = round(size / 1024, 1)
                if size_kb > 100:
                    file_size = " 📄"
                elif size_kb > 50:
                    file_size = " 📃"
                else:
                    file_size = " 📄"
            except:
                pass

            print(f"{prefix}{connector}[缺翻译] {item['english'].name}{file_size}")

    # 打印各个目录
    for dir_name, files in sorted(dir_structure.items()):
        print(f"📁 {dir_name}/")
        print_tree(files, prefix="│   ")
        print()

    print("=" * 80)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="查找项目中缺少中文翻译的 .md 文件并创建翻译任务",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--root', '-r',
        default='.',
        help='要扫描的根目录 (默认: 当前目录)'
    )

    args = parser.parse_args()

    print("🚀 开始翻译检查流程...")
    print(f"📁 根目录: {os.path.abspath(args.root)}")
    print("-" * 60)

    # 步骤1: 查找所有 .md 文件
    missing_files = find_missing_translations(args.root)

    # 步骤2: 打印目录树
    print_tree_structure(missing_files)

    # 步骤3: 创建翻译任务
    task_configs = create_translation_tasks(missing_files)

    if task_configs:
        print(f"\n🎯 发现 {len(task_configs)} 个翻译任务")
        print("💡 提示: 可以使用以下命令并行处理这些任务:")
        print("   python -m concurrent.futures process_tasks")
        print("   或手动分配给不同的翻译人员处理")
    else:
        print("\n✅ 所有文件都有对应的中文翻译！")

if __name__ == "__main__":
    main()