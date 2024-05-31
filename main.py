import os
import shutil


def find_and_show_subfolders(base_folder):
    for root, dirs, files in os.walk(base_folder):
        print(root)
        if "wallets" in dirs or "plugins" in dirs:
            if "wallets" in dirs:
                target_folder = "wallets"
            else:
                target_folder = "plugins"

            target_folder_path = os.path.join(root, target_folder)
            subfolders_path = os.path.join(target_folder_path)
            subfolders = [subfolder for subfolder in os.listdir(subfolders_path) if os.path.isdir(os.path.join(subfolders_path, subfolder))]

            if subfolders:
                for subfolder in subfolders:
                    new_folder_name = f"../../{result_folder}/{subfolder}"
                    new_folder_path = os.path.join(root, new_folder_name)
                    os.makedirs(new_folder_path, exist_ok=True)
                    root_dir = root.split('\\')[1]
                    shutil.copytree(root, f"{result_folder}/{subfolder}\{root_dir}")
                    print(f" - {subfolder}")

base_folder = "base"
result_folder = "result"

find_and_show_subfolders(base_folder)
