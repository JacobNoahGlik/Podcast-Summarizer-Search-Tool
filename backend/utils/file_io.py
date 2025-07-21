import os

def save_uploaded_file(uploaded_file, directory="examples/uploads"):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, uploaded_file.filename)
    uploaded_file.save(file_path)
    return file_path
