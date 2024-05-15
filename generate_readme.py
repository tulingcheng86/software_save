import os
import urllib.parse

def generate_readme(root_dir, output_file):
    readme_lines = ["# DailyWork\n"]

    def add_to_readme(path, level):
        indent = "  " * level
        if os.path.isdir(path):
            # 排除 .git 目录
            if os.path.basename(path) == '.git':
                return
            rel_path = os.path.relpath(path, root_dir)
            rel_path_encoded = urllib.parse.quote(rel_path)
            readme_lines.append(f"{indent}- **[{os.path.basename(path)}]({rel_path_encoded})**")
            for item in sorted(os.listdir(path)):
                item_path = os.path.join(path, item)
                # 只列出当前目录的内容
                if os.path.isdir(item_path) and os.path.basename(item_path) != '.git':
                    add_to_readme(item_path, level + 1)
                elif not os.path.isdir(item_path) and not item_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    item_rel_path = os.path.relpath(item_path, root_dir)
                    item_rel_path_encoded = urllib.parse.quote(item_rel_path)
                    readme_lines.append(f"{indent}  - [{os.path.basename(item_path)}]({item_rel_path_encoded})")
        else:
            # 排除图片文件
            if not path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp','.txt')):
                rel_path = os.path.relpath(path, root_dir)
                rel_path_encoded = urllib.parse.quote(rel_path)
                readme_lines.append(f"{indent}- [{os.path.basename(path)}]({rel_path_encoded})")

    # 仅列出当前目录的内容
    for item in sorted(os.listdir(root_dir)):
        add_to_readme(os.path.join(root_dir, item), 0)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(readme_lines))

if __name__ == "__main__":
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "README.md")
    generate_readme(current_dir, output_file)

