#!/usr/bin/env python3
"""
简单的翻译任务生成脚本
"""

import os
from pathlib import Path
import json
from datetime import datetime

def find_missing_translations():
    """查找缺少中文翻译的文件"""
    print("🔍 查找缺少的翻译文件...")

    root_dir = Path(".")
    missing_files = []

    # 需要排除的文件
    excluded_files = {
        'LICENSE.md', 'README.md', 'CLAUDE.md',
        'docs/examples.md', 'docs/scientific-skills.md'
    }

    for md_file in root_dir.rglob("*.md"):
        # 跳过已有翻译和排除的文件
        if (md_file.name.endswith('.zh.md') or
            md_file.name in excluded_files or
            '.git' in str(md_file)):
            continue

        # 检查中文翻译是否存在
        zh_file = md_file.with_suffix('.zh.md')
        if not zh_file.exists():
            relative_path = str(md_file.relative_to(root_dir))
            if 'scientific-skills/' in relative_path:  # 只处理技能目录
                size_kb = md_file.stat().st_size // 1024 if md_file.exists() else 0
                missing_files.append({
                    'english': str(md_file),
                    'chinese_expected': str(zh_file),
                    'relative_path': relative_path,
                    'size_kb': size_kb
                })

    print(f"找到 {len(missing_files)} 个需要翻译的文件")
    return missing_files

def create_tasks(missing_files):
    """创建5个翻译任务"""
    if not missing_files:
        print("✅ 所有文件都有对应的中文翻译！")
        return []

    print(f"📝 创建 {min(5, len(missing_files))} 个翻译任务...")

    # 按5个任务分配文件
    tasks = []
    for i in range(5):
        start_idx = i * (len(missing_files) // 5)
        end_idx = start_idx + (len(missing_files) // 5)
        if i < (len(missing_files) % 5):
            end_idx += 1

        if start_idx < len(missing_files):
            task_files = missing_files[start_idx:end_idx]
        else:
            task_files = []

        tasks.append({
            'task_id': i + 1,
            'files': task_files,
            'count': len(task_files)
        })

    # 分配剩余的文件
    if len(missing_files) > 5:
        for i, extra_file in enumerate(missing_files[5 * (len(missing_files) // 5):]):
            task_idx = i % 5
            tasks[task_idx]['files'].append(extra_file)
            tasks[task_idx]['count'] += 1

    return tasks

def main():
    print("🚀 开始生成翻译任务...")

    # 查找缺少翻译的文件
    missing_files = find_missing_translations()

    if missing_files:
        # 创建任务
        tasks = create_tasks(missing_files)

        # 生成任务配置
        config = {
            'created_at': datetime.now().isoformat(),
            'total_missing_files': len(missing_files),
            'tasks': tasks
        }

        # 保存配置
        with open('translation_tasks.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        # 显示摘要
        print(f"📊 任务配置已保存到 translation_tasks.json")
        print(f"📋 总计: {config['total_missing_files']} 个文件需要翻译")
        print()
        print("📝 任务分配:")
        for task in tasks:
            files_list = [f['relative_path'] for f in task['files'][:5]]
            if len(task['files']) > 5:
                files_list += f" ... 还有 {len(task['files']) - 5} 个文件"
            print(f"任务 {task['task_id']}: {task['count']} 个文件")
            for file_path in files_list:
                print(f"  - {file_path}")
            print()

        print(f"💡 提示: 可以使用以下命令处理这些任务:")
        print("  python -m concurrent.futures process_tasks")
        print("  或手动分配给不同的翻译人员处理")
    else:
        print("✅ 所有文件都有对应的中文翻译！")

if __name__ == "__main__":
    main()