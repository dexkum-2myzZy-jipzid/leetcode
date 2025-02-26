#!/usr/bin/env python3

import os


def create_file(filename, user="Mario", extension="py"):
    # Step 2: Replace spaces with underscores
    filename = filename.replace(" ", "_")

    # Step 3: Remove the first occurrence of an underscore
    filename = filename.replace("_", "", 1)

    print(f"filename:{filename}")

    # Step 4: Create the directory
    directory = f"LeetCode/{filename}/{user}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Step 5: Create the file
    file_extension = extension
    file_path = f"{directory}/{filename}.{file_extension}"
    with open(file_path, 'w') as file:
        pass

    # If the file is a Python script, add the shebang line
    if file_extension == "py":
        with open(file_path, 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write("#!/usr/bin/env python3\n" + content)

    return f"File created at {file_path}"


# Example usage
filename = input("Enter the filename: ")
# user = input("Enter the username (default is Mario): ")
# user = user if user else "Mario"
# extension = input("Enter the extension of language (default is python): ")
# extension = extension if extension else "py"
user = "Mario"
extension = "py"
create_file(filename, user, extension)
