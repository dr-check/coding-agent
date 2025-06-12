# Function to get information about files in a directory, including absolute path and file size.

import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_target_path = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_target_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{abs_target_path}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target_path):
        return f'Error: "{abs_target_path}" is not a directory'
    
    list_dir = os.listdir(abs_target_path)
    meta_list = []
    for item in list_dir:
        item_path = os.path.join(abs_target_path, item)
        file_size  = os.path.getsize(item_path)
        file_type = True if os.path.isdir(item_path) else False
        meta_list.append(f"{item}: file_size={file_size}, is_dir={file_type}")
    return "\n".join(meta_list)



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
