import os
import math
import shutil

basepath = raw_input("Give Me the Directory Please: ")
print(basepath)
# List all files in a directory using os.listdir
#basepath = 'my_directory/'
#basepath = basepath.replace('\\', '/');
print(basepath)

MAX_PER_DIR = 15000

filelist = os.listdir(basepath);
numdirs = math.ceil(len(filelist) / MAX_PER_DIR)
print("len(filelist): " + str(len(filelist)) )
print("numdirs: " + str( numdirs ) )

for x in range(int(numdirs)):
    dirname = os.path.basename(basepath)+"-"+str(int(x+1))
    dirNameToMake = os.path.join(basepath, dirname)
    print("************************************")
    print("dirname: " + dirname)
    print("dirNameToMake: " + dirNameToMake)
    os.mkdir(dirNameToMake)
    count = 1
    for entry in os.listdir(basepath):
        fileToBeMoved = os.path.join(basepath, entry)
        filePathAfterMoved = os.path.join(dirNameToMake, entry)
        if os.path.isfile(fileToBeMoved):
            shutil.move(fileToBeMoved, filePathAfterMoved)
            count = count+1
            if count % 250 == 0 :
                print(str(count) + " of " + str(len(filelist)) + " done ")
            if (count % MAX_PER_DIR == 0) :
                break;
    print("************************************")
