import os
import shutil

WIKI_ROOT = '/home/zf-li23/freedom/personal-wiki-site/docs/wiki'

def migrate_to_index_md():
    # Walk top-down. 
    # We need to be careful not to modify the list while iterating, so we collect moves first.
    moves = []

    for root, dirs, files in os.walk(WIKI_ROOT):
        for file in files:
            if file == 'index.md':
                continue
            if not file.endswith('.md'):
                continue
            
            file_path = os.path.join(root, file)
            file_name_no_ext = file[:-3] # remove .md
            target_dir = os.path.join(root, file_name_no_ext)
            
            # If directory exists, move file into it as index.md
            if os.path.exists(target_dir):
                if not os.path.exists(os.path.join(target_dir, 'index.md')):
                    moves.append((file_path, os.path.join(target_dir, 'index.md')))
                else:
                    print(f"Skipping {file_path}: {target_dir}/index.md already exists")
            else:
                # Directory does not exist. Create it and move file.
                moves.append((file_path, os.path.join(target_dir, 'index.md')))

    for src, dst in moves:
        print(f"Migrating {src} -> {dst}")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)

if __name__ == '__main__':
    migrate_to_index_md()
