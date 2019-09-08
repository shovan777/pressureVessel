"""Simple wrapper to read and write files."""
import os
# import json
from django.conf import settings
from django.core.files.storage import default_storage

IS_PRODUCTION = settings.PRODUCTION

def create_file(file_path, content):
    """Make dir and write content into file."""
    if IS_PRODUCTION:
        try:
            file = default_storage.open(file_path, 'w')
            file.write(content)
        except Exception as error:
            raise error
        finally:
            file.close()
    else:
        folder = os.path.split(file_path)[0]
        os.makedirs(folder, exist_ok=True)
        if isinstance(content, bytes):
            content = content.decode()
        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as error:
            raise error

def write_file(file_path, content):
    """Write content into file."""
    # print(IS_PRODUCTION)
    if IS_PRODUCTION:
        try:
            file = default_storage.open(file_path, 'w')
            file.write(content)
        except Exception as error:
            raise error
        finally:
            file.close()
    else:
        if isinstance(content, bytes):
            content = content.decode()
        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as error:
            raise error

def delete_file():
    """Delete files."""
    # this method deletes files

def read_file(file_path):
    """Read content from the given path."""
    if IS_PRODUCTION:
        try:
            file = default_storage.open(file_path, 'r')
            content = file.read()
            file.close()
        except Exception as error:
            # print(e)
            raise error
        # finally:
        #     file.close()
    else:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except Exception as error:
            # print(e)
            raise error
        if isinstance(content, str):
            content = content.encode()
    return content
    # this method reads the file and gives back the content


