"""
Module for handling files, directories and databases
"""

import os
from leventools.tools.file_handling import working_directory

def test_working_directory():
    cwd = os.getcwd()
    with working_directory('C://'):
        print('Test Run')
    assert os.getcwd() == cwd