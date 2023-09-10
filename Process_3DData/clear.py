import os

def delete_files_in_folders(folders):
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

# Example usage
folders_to_clean = ["./AR", "./depth", "./pre_depth", "./pre_rgb", "./front_depth", "./front_rgb" ]
delete_files_in_folders(folders_to_clean)
