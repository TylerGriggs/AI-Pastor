# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:00:02 2019

This script is designed to remove empty lines, as well as time-stamp lines from
.sbv generated automatically from YouTube speach to text.

@author: Tyler Griggs
"""
import glob
import os

def format_subtitles(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: not ":" in x, lines)
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


path = os.path.dirname(os.path.abspath(__file__))
txtlist = glob.glob(path + '\*.sbv')

for file in txtlist:
    format_subtitles(file)

with open('output.txt', 'w') as outfile:
    for file in txtlist:
        with open(file) as infile:
            outfile.write(infile.read())
    

