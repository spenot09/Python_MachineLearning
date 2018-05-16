import random

#define a function that will concatenate a list of files
def csvConcat(filenames, output_dir):
    with open(output_dir, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def fileRandomiser(fname, output_dir):
    lines = open(fname).readlines()
    random.shuffle(lines)
    open(output_dir, 'w').writelines(lines)

def fileSplitter(fname, output_name):

    input = open(fname, 'r').read()
    splitLen = len(input)/2         # half of the file
    outputBase = output_name # output.1.txt, output.2.txt, etc.

    count = 0
    at = 0
    dest = None
    for line in input:
        if count % splitLen == 0:
            if dest: dest.close()
            dest = open(outputBase + str(at) + 'Half.csv', 'w')
            at += 1
        dest.write(line)
        count += 1


filenames_Chew = []
filenames_Not_Chew = []
filenames_Overall = ['/user/HS127/sc00858/OpenPose/Output/Train/NotChew_dataset/allNotChewPoints.csv', '/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/allChewPoints.csv']

#files to loop through
fls=['04','08', '09', '10', '11','12', '16', '17','18', '19', '20', '21', '22', '23']

#create lists of the files to concatenate
for i in fls:
    fNotChew_dir= ("/user/HS127/sc00858/OpenPose/Output/Train/NotChew_dataset/datasetNotChew%s.csv" % i)
    fChew_dir=  ("/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/datasetChew%s.csv" % i)
    filenames_Not_Chew.append(fNotChew_dir)
    filenames_Chew.append(fChew_dir)

#call functions to concatenate files
csvConcat(filenames_Not_Chew, '/user/HS127/sc00858/OpenPose/Output/Train/NotChew_dataset/allNotChewPoints.csv')
csvConcat(filenames_Chew, '/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/allChewPoints.csv')

fileRandomiser('/user/HS127/sc00858/OpenPose/Output/Train/NotChew_dataset/allNotChewPoints.csv', '/user/HS127/sc00858/OpenPose/Output/Train/NotChew_dataset/allNotChewPoints Random.csv')
fileRandomiser('/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/allChewPoints.csv', '/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/allChewPointsRandom.csv')

fileSplitter('/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/allChewPointsRandom.csv', '/user/HS127/sc00858/OpenPose/Output/Train/chewRandom')
fileSplitter('/user/HS127/sc00858/OpenPose/Output/Train/NotChew_dataset/allNotChewPointsRandom.csv', '/user/HS127/sc00858/OpenPose/Output/Train/notChewRandom')

filenames_train = ['/user/HS127/sc00858/OpenPose/Output/Train/chewRandom0Half.csv', '/user/HS127/sc00858/OpenPose/Output/Train/notChewRandom0Half.csv']
filenames_test = ['/user/HS127/sc00858/OpenPose/Output/Train/chewRandom1Half.csv', '/user/HS127/sc00858/OpenPose/Output/Train/notChewRandom1Half.csv']

csvConcat(filenames_train, '/user/HS127/sc00858/OpenPose/Output/Train/training_set.csv')
csvConcat(filenames_test, '/user/HS127/sc00858/OpenPose/Output/Train/testing_set.csv')
