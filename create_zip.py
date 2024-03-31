# create_zip.py  
import zipfile  
import os  
  
def create_zip_with_relative_path(zip_filename, relative_path):  
    with zipfile.ZipFile(zip_filename, 'w') as zipf:  
        abs_path = os.path.abspath(relative_path)  
        if os.path.exists(abs_path):  
            if os.path.isfile(abs_path):  
                zipf.write(abs_path, arcname=os.path.relpath(abs_path, os.path.dirname(relative_path) + '/../'))  
            elif os.path.isdir(abs_path):  
                for root, dirs, files in os.walk(abs_path):  
                    for file in files:  
                        file_path = os.path.join(root, file)  
                        arcname = os.path.relpath(file_path, os.path.dirname(relative_path) + '/../')  
                        zipf.write(file_path, arcname=arcname)  
        else:  
            print(f"Path '{abs_path}' does not exist.")  
  
# 调用函数创建ZIP文件  
create_zip_with_relative_path('my_archive.zip', '../../path/to/your/file_or_folder')