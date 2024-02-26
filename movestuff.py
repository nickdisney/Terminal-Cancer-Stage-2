import os

# Define the current file path and the new file path
current_file_path = '/Users/nick/Desktop/aimee/aimaze/dolphinkiller/Terminal-Cancer/templates/index.html.txt'
new_file_path = '/Users/nick/Desktop/aimee/aimaze/dolphinkiller/Terminal-Cancer/templates/index.html'

# Rename the file
os.rename(current_file_path, new_file_path)

# Corrected print statement
print(f"File renamed to: {new_file_path}")
