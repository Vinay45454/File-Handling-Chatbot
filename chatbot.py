import spacy
import os
import shutil

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the intents and corresponding file management actions

# Define the file management functions
def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('')
        return f"File '{file_name}' created successfully."
    except Exception as e:
        return str(e)

def delete_file(file_name):
    try:
        os.remove(file_name)
        return f"File '{file_name}' deleted successfully."
    except Exception as e:
        return str(e)

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        return f"File '{old_name}' renamed to '{new_name}' successfully."
    except Exception as e:
        return str(e)

def list_files(directory='.'):
    try:
        files = os.listdir(directory)
        if files:
            return f"Files in directory '{directory}':\n{', '.join(files)}"
        else:
            return f"No files found in directory '{directory}'."
    except Exception as e:
        return str(e)

def check_file(file_name):
    try:
        if os.path.isfile(file_name):
            return f"File '{file_name}' exists."
        else:
            return f"File '{file_name}' does not exist."
    except Exception as e:
        return str(e)

def get_file_info(file_name):
    try:
        if os.path.isfile(file_name):
            file_size = os.path.getsize(file_name)
            file_modified = os.path.getmtime(file_name)
            return f"File '{file_name}' information:\nSize: {file_size} bytes\nLast modified: {file_modified}"
        else:
            return f"File '{file_name}' does not exist."
    except Exception as e:
        return str(e)

def move_file(file_name, destination):
    try:
        shutil.move(file_name, destination)
        return f"File '{file_name}' moved to '{destination}' successfully."
    except Exception as e:
        return str(e)

def remove_directory(directory):
    try:
        shutil.rmtree(directory)
        return f"Directory '{directory}' removed successfully."
    except Exception as e:
        return str(e)
intents = {
    'create': create_file,
    'delete': delete_file,
    'rename': rename_file,
    'list': list_files,
    'check': check_file,
    'info': get_file_info,
    'move': move_file,
    'remove': remove_directory
}

def process_user_input(user_input):
    doc = nlp(user_input)
    tokenized_input = [token.text for token in doc]
    response = ""

    if len(tokenized_input) == 0:
        response = "Please enter a command."
    elif len(tokenized_input) == 1:
        response = "Please provide a file name."
    else:
        action = tokenized_input[0].lower()
        file_name = tokenized_input[1]

        if action in intents:
            if action in ['list', 'check', 'info']:
                response = intents[action](file_name)
            elif len(tokenized_input) >= 3:
                new_name = tokenized_input[2]
                response = intents[action](file_name, new_name)
            else:
                response = "Please provide a new file name for renaming."
        else:
            response = "Invalid command."

    return response
