from cli import parse_argv
import face_recognition
from os import walk

# default settings
default_settings = {
    "work": "Mail",
    "leis": "Google Chrome",
    "show": False,
    "rest": 0.5,
    "safe": True,
}

# get user input arguments
arguments = parse_argv()


def option(opt):
    """get value from arguments; if not set, get if from the default settings

    Args:
        opt (str): The option name that is going to get.
    """

    # get global variables
    global arguments, default_settings

    # check if user input has the option
    if opt in arguments:
        return arguments[opt]

    # otherwise use the default settings
    else:
        return default_settings[opt]


def load_and_encode():
    """Load and encode faces in ignore file.

    Returns:
        list: List of all encoded faces in ignore file.
    """

    faces = []

    # load files + encode
    for _, _, names in walk("ignore"):
        for name in names:
            if name == '.gitignore':
                continue
            img = face_recognition.load_image_file('ignore/' + name)
            for face_encoding in face_recognition.face_encodings(img):
                faces.append(face_encoding)

    return faces


# load images
ignored_faces = load_and_encode()


def is_ignored_faces(faces):
    """Check if the faces are ignored faces.

    Args:
        faces: Encoded face from face_recognition.

    Returns:
        bool: If a not ignored face appeared, return false, otherwise true.
    """

    global ignored_faces
    for face in faces:
        matches = face_recognition.compare_faces(ignored_faces, face)
        if False in matches:
            return False
    return True
