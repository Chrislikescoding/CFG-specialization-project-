import csv
import os
from os.path import join
def get_tree_data(self):
    path = os.getcwd()
    path: str = join(path, 'extracted_data.csv')
    File = open(str(path))
    Reader = csv.reader(File)
    Data = list(Reader)
    return Data
