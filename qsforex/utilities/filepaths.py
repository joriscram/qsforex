# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:48:30 2015

@author: jorisc
"""
from os import path, listdir
from Tkinter import Tk
from tkFileDialog import askopenfilename

_ROOT = path.split(path.split(path.abspath(path.dirname(__file__)))[0])[0]
RESOURCES = path.join(_ROOT, 'resources')
INPUT = path.join(RESOURCES, 'input')
OUTPUT = path.join(RESOURCES, 'output')
DATA = path.join(RESOURCES, 'data')
TEST = path.join(RESOURCES, 'test')

"""
In order to support both windows and linux paths should always be constructed with the os.path functionality
typically the rescource folder contains subfolders.

Below an example of a generic function returning a relative path is shown:
"""
def get_data(filename):
    filepath =  path.join(DATA, filename)
    return filepath

def get_list_csv():
    return listdir(DATA)

def get_test_data(filename):
    filepath =  path.join(TEST, filename)
    return filepath

def get_output_path(filename):
    filepath =  path.join(OUTPUT, filename)
    return filepath

def askforinput():
	Tk().withdraw()
	file_name = askopenfilename(initialdir = INPUT , title = 'Open a csv file')
	return file_name