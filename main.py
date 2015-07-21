__author__ = 'cpalmer'
import openFile
import parseString

filename = raw_input("filename: ")

file_as_string = openFile.get_file_as_string(filename)

parseString.error_check(file_as_string)

