import pprint

def get_cats_info(path):
    try:
        # Open the file with the specified path in read mode with UTF-8 encoding
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                # Split the line by comma to get id, name, and age
                id, name, age = line.strip().split(',')
                # Create a dictionary for each cat with keys "id", "name", and "age"
                cat_info = {"id": id, "name": name, "age": age}
                # Append the dictionary to the list of cats
                cats.append(cat_info)
        return cats
    except FileNotFoundError:
        # If the file is not found, print an error message and return an empty list
        print(f"File with path {path} was not found.")
        return []
    except Exception as e:
        # If any other error occurs, print the error message and return an empty list
        print(f"An error occurred during file processing: {e}")
        return []

# Specify the relative path to the file
file_path = "module_4/second_hw/cats_file.txt"
cats_info = get_cats_info(file_path)
pprint.pp(cats_info)
