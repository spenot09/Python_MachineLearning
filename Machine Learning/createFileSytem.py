import os
import fnmatch
import shutil

fname="/user/HS127/sc00858/OpenPose/Code/MVI_0023"


notChewFile= ("/user/HS127/sc00858/OpenPose/Output/%s/NotChew_%s" % (fname[-8:], fname[-8:]))

if not os.path.exists(notChewFile):
    os.makedirs(notChewFile)
