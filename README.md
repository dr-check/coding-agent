# Coding Agent
This coding agent was built as a tool to aid in minor bug fixing on a local machine. In order to do achieve this, it needs access to the files and folders in your workspace so the code will require some editing to change filepaths. This tool was the result of a project assigned by the Boot.dev backend education path, and is therefore NOT a product recommended for use as it lacks any of the security features a true agent would have.

## Prerequisites
Before you begin, make sure you set the agent to only have access to the specific filepaths you want it to. Out of the box, it should be unable to access anything as the default filepath names are unlikely to match anything on your system.

This project is built in python 3 and uses the Gemini API mainly because Gemini is free and I am cheap.

## Using the Agent

Like most other AI tools, simply explain to the agent what you want, and it should be able to do it. If you run into any roadblocks, you can always edit the system-level prompt to update its primary behaviors.


## Note on Security
As stated above, this is a student project created for educational purposes and does not include any security features. I do not recommend giving an unknown AI agent access to any of your system's files or folders.
