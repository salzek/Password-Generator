from gui_ import startGui
from variables import ROOT_DIR
from os import mkdir
import os.path as path

fname3 = ROOT_DIR+"\\output"
if not path.isdir(fname3):
    mkdir(fname3)
fname3 = ROOT_DIR+"\\raw-files"
if not path.isdir(fname3):
    mkdir(fname3)

startGui()




 