import os
import shutil

def organize_files(folder_path):
    try:
        # Create folders if they don't exist
        images_folder = os.path.join(folder_path, "Images")
        documents_folder = os.path.join(folder_path, "Documents")
        os.makedirs(images_folder, exist_ok=True)
        os.makedirs(documents_folder, exist_ok=True)

        # Organize files
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                if filename.endswith((".jpg", ".png")):
                    shutil.move(file_path, images_folder)
                elif filename.endswith((".docx", ".pdf")):
                    shutil.move(file_path, documents_folder)
        print("Files organized successfully.")
    except Exception as e:
        print(f"Error organizing files: {e}")

def main():
    folder_path = input("Enter the folder path: ")
    organize_files(folder_path)

if __name__ == "__main__":
    main()