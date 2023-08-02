import os 
import shutil
source_dir = "C:/Users/Admin/Downloads"
destination_dir = "C:/python programes"
list_of_files = os.listdir(source_dir)
#print(list_of_files)

for file in list_of_files:
    name,extension = os.path.splitext(file)
    print(name)
    print(extension)
