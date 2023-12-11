import os
import shutil


class FileManager:
    def __init__(self, current_directory='.'):
        self.current_directory = current_directory

    def list_contents(self):
        return os.listdir(self.current_directory)

    def create_directory(self, directory_name):
        os.makedirs(os.path.join(self.current_directory, directory_name))

    def delete_item(self, item_name):
        item_path = os.path.join(self.current_directory, item_name)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

    def copy_item(self, item_name, destination):
        shutil.copy2(os.path.join(self.current_directory, item_name), destination)

    def move_item(self, item_name, destination):
        shutil.move(os.path.join(self.current_directory, item_name), destination)

    def search_file(self, file_name):
        for root, dirs, files in os.walk(self.current_directory):
            if file_name in files:
                return os.path.join(root, file_name)
        return None

    def change_access_rights(self, item_name, permissions):
        item_path = os.path.join(self.current_directory, item_name)
        os.chmod(item_path, permissions)

    def print_access_rights(self, item_name):
        item_path = os.path.join(self.current_directory, item_name)
        permissions = oct(os.stat(item_path).st_mode & 0o777)
        print(f"{item_name} access rights: {permissions}")
