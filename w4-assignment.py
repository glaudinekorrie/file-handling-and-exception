def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Example Modification: Convert text to uppercase
        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read the file.")

# Run the function
read_and_modify_file()
