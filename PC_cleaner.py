import os
import shutil
import psutil

def clean_temp_files():
    temp_folders = [os.getenv('TEMP'), os.getenv('TMP')]
    print("Cleaning temporary files...")
    for temp_folder in temp_folders:
        if temp_folder and os.path.exists(temp_folder):
            for root, dirs, files in os.walk(temp_folder):
                for name in files:
                    file_path = os.path.join(root, name)
                    try:
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                    except Exception as e:
                        print(f"Failed to delete file: {file_path}. Reason: {e}")
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    try:
                        shutil.rmtree(dir_path)
                        print(f"Deleted directory: {dir_path}")
                    except Exception as e:
                        print(f"Failed to delete directory: {dir_path}. Reason: {e}")
        else:
            print(f"Temporary folder {temp_folder} does not exist.")

def optimize_memory():
    print("Optimizing memory...")
    process = psutil.Process(os.getpid())
    process_memory_info = process.memory_info()
    print(f"Memory usage before optimization: {process_memory_info.rss / (1024 ** 2):.2f} MB")
    
    # Clear the page cache, dentries and inodes
    with open('/proc/sys/vm/drop_caches', 'w') as f:
        f.write('3\n')
    
    process_memory_info = process.memory_info()
    print(f"Memory usage after optimization: {process_memory_info.rss / (1024 ** 2):.2f} MB")

def main():
    clean_temp_files()
    optimize_memory()
    print("PC optimization complete.")

if __name__ == "__main__":
    main()