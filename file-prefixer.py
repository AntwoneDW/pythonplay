import os
import math
import shutil

MAX_PER_DIR = 12013

basepath = raw_input("Give Me the Directory Please: ")
print(basepath)
fileprefix = raw_input("What Do You want to prefix files with? ")
print(fileprefix)
copyOrRename = raw_input("Do you want a copy (C) or do you want to rename? (R) ")
print(copyOrRename)
outPath = raw_input("Output Path? ")
print(outPath)

filelist = os.listdir(basepath);

for entry in os.listdir(basepath):
    fileToBeMoved = os.path.join(basepath, entry)
    dirToPutIt = basepath
    if outPath:
        dirToPutIt = outPath
    filePathAfterMoved = os.path.join(basepath, (fileprefix + entry))
    if os.path.isfile(fileToBeMoved):
        if(copyOrRename.lower() == "R"):
            shutil.move(fileToBeMoved, filePathAfterMoved)
        else:
            shutil.copy(fileToBeMoved, filePathAfterMoved)
    print('moved ' + fileToBeMoved + " to " + filePathAfterMoved);
print("************************************")
