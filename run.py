import os
import shutil
import subprocess

# Define paths
images_dir = 'D:/IIndicus/Đồ án/web app with model/media/images'
db_file = 'D:/IIndicus/Đồ án/web app with model/db.sqlite3'

# Function to delete files in a directory
def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Delete subdirectories
            else:
                os.remove(file_path)  # Delete files
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def delete_all_images_in_media(media_directory):
    if not os.path.exists(media_directory):
        return

    # Define common image file extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    
    for root, dirs, files in os.walk(media_directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# Function to run shell commands
def run_shell_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully ran: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {command}: {e}")

# Step 1: Delete all files in the images and thumbnails directories
delete_files_in_directory(images_dir)

# Step 2: Delete db.sqlite3
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"Deleted {db_file}")
else:
    print(f"{db_file} not found.")

# Step 3: Run migrations
run_shell_command('python manage.py migrate')

# Step 4: Run the server
#run_shell_command('python manage.py runserver')
