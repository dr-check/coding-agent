# This function allows the agent to run Python code.

import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_path = os.path.abspath(working_directory)
    path = file_path if os.path.isabs(file_path) else os.path.join(abs_path, file_path)
    full_path = os.path.abspath(path)

    if os.path.commonpath([abs_path, full_path]) != abs_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if os.path.exists(full_path) == False:
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            ["python", full_path],
            cwd=abs_path,
            capture_output=True, 
            timeout=30,
            check=False,
        )
        
        output = result.stdout.decode('utf-8')
        errors = result.stderr.decode('utf-8')
        exit_code = result.returncode

        if not result.stdout and not result.stderr:
            return 'No output produced.'
        
        if not result.stdout and result.stderr:
            if exit_code != 0:
                return f'STDERR: {errors}\nProcess exited with code {exit_code}'
            return f'STDERR: {errors}'
        
        if result.stdout and not result.stderr:
            if exit_code != 0:
                return f'STDOUT: {output}\nProcess exited with code {exit_code}'
            return f'STDOUT: {output}'
    
        if exit_code != 0:
            return f'STDOUT: {output}\nSTDERR: {errors}\nProcess exited with code {exit_code}'
        return f'STDOUT: {output}\nSTDERR: {errors}'
    
    except Exception as e:
        return f"Error: executing python file: {e}"
    


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file in the specified directory. The file must be a valid Python script.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
    ),
)