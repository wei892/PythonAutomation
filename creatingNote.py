import os
from pathlib import Path

# Get the current directory
current_directory = Path.cwd()
# print(current_directory.iterdir())

# Iterate over each item in the directory
for item in current_directory.iterdir():
    print(item)
    # Check if the item is a directory
    if item.is_dir():
        # Define the path for the new note.txt file
        note_path = item / 'note.txt'
        # Create a note.txt file if it does not exist
        with note_path.open('a') as file:
            file.write("Chapter .\n")

print("note.txt files added to all directories.")
