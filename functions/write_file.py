# This function will allow the agent to write to files.

import os

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(working_directory)
    path = file_path if os.path.isabs(file_path) else os.path.join(abs_path, file_path)
    full_path = os.path.abspath(path)

    if os.path.commonpath([abs_path, full_path]) != abs_path:
        return f'Error: Cannot write to "{full_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'

    return f'Successfully wrote to "{full_path}" ({len(content)} characters written)'