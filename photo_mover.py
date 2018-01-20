# ----------------------------------------------
# Imports
# ----------------------------------------------

from resources.libraries.common import logging_lib
from resources.libraries.common import path_utils

# ----------------------------------------------
# Constants
# ----------------------------------------------

PHOTO_TK_LOGGER_NAME = "PTKLogger"
LOGGER = logging_lib.Logger(PHOTO_TK_LOGGER_NAME)

# ----------------------------------------------
# Main
# ----------------------------------------------

if __name__ == '__main__':
    l = path_utils.get_all_files_from_path("C:/", "lrcat", True)
    for a in l:
        print(a)
    # path_utils.copy_files_into_folder(l, "C:/Users/Jachiev/Desktop/copy")

