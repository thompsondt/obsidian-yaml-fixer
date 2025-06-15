import os
import re
import sys
from datetime import datetime

def correct_created_field(file_path):
    # Open and read the markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract the front matter from the beginning of the file
    front_matter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    
    if front_matter_match:
        front_matter = front_matter_match.group(1)
        
        # Extract 'date' and 'created' fields
        date_match = re.search(r'^date:\s*(.+)', front_matter, re.MULTILINE)
        created_match = re.search(r'^created:\s*(.+)', front_matter, re.MULTILINE)

        if date_match and created_match:
            date_value = date_match.group(1).strip()
            created_value = created_match.group(1).strip()

            # Parse the 'date' value into a datetime object, considering its format
            try:
                parsed_date = datetime.strptime(date_value, '%Y-%m-%d %H:%M:%S %A')
            except ValueError as e:
                print(f"Error parsing date in file '{file_path}': {e}")
                return

            # Preserve the format of 'created' and create a new value
            try:
                # Determine the format of 'created' by parsing it
                if 'T' in created_value:
                    created_format = '%Y-%m-%dT%H:%M:%S'
                else:
                    created_format = '%Y-%m-%d %H:%M:%S'

                # Parse the original 'created' value to ensure the format is correct
                datetime.strptime(created_value, created_format)
                
                new_created_value = parsed_date.strftime(created_format)
            except ValueError as e:
                print(f"Error parsing created in file '{file_path}': {e}")
                return
            
            # Replace the old 'created' value with the new one
            updated_front_matter = re.sub( r'^(created:\s*).+$', f"created: {new_created_value}", front_matter,
                                          flags=re.MULTILINE)
            updated_content = content.replace(front_matter_match.group(1), updated_front_matter)

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Updated 'created' field in file: {file_path}")
        else:
            print(f"Could not find 'date' or 'created' fields in file: {file_path}")
    else:
        print(f"No front matter found at the beginning of file: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                correct_created_field(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py path/to/markdown/files")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' is not a directory.")
        sys.exit(1)
    process_directory(directory)
