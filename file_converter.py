import os

def find_extension(file):
    # Open the file in binary mode
    with open(file, "rb") as f:
        # Read the first 4 bytes
        hex_code = f.read(4).hex()

        # Check the hex code against a set of known codes
        # and return the corresponding extension
        if hex_code == "89504e47":
            return ".png"
        elif hex_code == "47494638":
            return ".gif"
        elif hex_code == "ffd8ffe0" or hex_code == "ffd8ffe1":
            return ".jpeg"
        elif hex_code == "25504446":
            return ".pdf"
        elif hex_code == "4d4d002a" or hex_code == "49492a00":
            return ".tiff"
        else:
            # If no matching hex code is found, return an empty string
            return ""

def save_file(file, extension, new_directory):
    # Split the original file name and path
    head, tail = os.path.split(file)
    file_name, old_extension = os.path.splitext(tail) # Remove the old extension
    # Generate the new file name with the extension
    new_file = os.path.join(new_directory, file_name + extension)
    # Copy the content of the original file to the new file
    with open(file, "rb") as src:
        with open(new_file, "wb") as dst:
            dst.write(src.read())

def process_directory(directory):
    # Create a new directory in the downloads section to save the files
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    new_directory = os.path.join(downloads, "converted_files")
    os.makedirs(new_directory, exist_ok=True)

    # Iterate over all files in the directory
    for file in os.listdir(directory):
        # Get the full file path
        file_path = os.path.join(directory, file)
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
            # Find the extension of the file
            extension = find_extension(file_path)
            if extension:
                # If the extension is found, save the file to the new directory
                save_file(file_path, extension, new_directory)
                print(f"The extension of {file} is {extension}")
            else:
                print(f"The extension of {file} could not be determined")

# Test the code with a sample directory
directory = "C:\Test Files"
process_directory(directory)
