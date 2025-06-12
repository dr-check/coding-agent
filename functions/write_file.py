# This function will allow the agent to write to files.

import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(working_directory)
    path = file_path if os.path.isabs(file_path) else os.path.join(abs_path, file_path)
    full_path = os.path.abspath(path)

    if os.path.commonpath([abs_path, full_path]) != abs_path:
        return f'Error: Cannot write to "{full_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{full_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the specified directory. If the file does not exist, it will be created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
                )
            },
        ),
    )