__author__ = 'cpalmer'
import os
import sys
current_path = os.path.dirname(os.path.abspath(__file__))


def get_file_as_string(filename):
    f = open(current_path+'/'+filename)
    return f.read()

