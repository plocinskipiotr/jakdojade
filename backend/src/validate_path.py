import os


def validate_path_file(path):
    if os.path.isfile(path) and os.access(path, os.R_OK):
        return path
    else:
        raise FileNotFoundError()


def validate_path(path):
    if os.path.isfile(path) and os.access(path, os.R_OK) or os.path.isdir(path):
        return path
    else:
        raise OSError('invalid path: ' + path)
