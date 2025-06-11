# This function reads the content of a file from a specified working directory.

import os

def get_file_content(working_directory, file_path):
    abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_target_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{abs_target_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_target_path):
        return f'Error: File not found or is not a regular file: "{abs_target_path}"'
    
    max_chars = 10000
    with open(abs_target_path, "r") as f:
        file_string = f.read(max_chars)
    
    if len(file_string) < max_chars:
        return file_string
    else:
        return file_string + f"\n[...File '{file_path}' truncated at 10000 characters]"