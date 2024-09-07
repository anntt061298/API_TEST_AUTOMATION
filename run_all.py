import os
import subprocess

# Get the current directory
current_dir = os.getcwd()

# Loop through all files in the current directory
for filename in os.listdir(current_dir):
    # Check if the file is a Python file and starts with 'test_'
    if filename.startswith('test_') and filename.endswith('.py'):
        # Run the Python file
        print("Running Test File: ", filename)
        subprocess.run(['python', filename])