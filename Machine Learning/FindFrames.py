import os
import fnmatch
import shutil

lst=[]

fname="/user/HS127/sc00858/OpenPose/Code/MVI_0023"

f= open(fname)
for content in f.readlines():
    # remove whitespace characters like `\n` at the end of each line and an extra space
    content=content.strip()
    lst.append(content)


chewFile= ("/user/HS127/sc00858/OpenPose/Output/%s/Chew_%s" % (fname[-8:], fname[-8:]))

#create new chewFile if not created yet
if not os.path.exists(chewFile):
    os.makedirs(chewFile)

#set directory to move files from below
notChewFile= ("/user/HS127/sc00858/OpenPose/Output/%s/NotChew_%s" % (fname[-8:], fname[-8:]))

#find json files that match chewing frames
for count in range(len(lst)):
    frameNum= lst[count]
    for file in os.listdir(notChewFile):
        if fnmatch.fnmatch(file, "*0%s_*" % frameNum):
            #cut and paste action
            shutil.move("%s/%s"%(notChewFile, file),chewFile)
