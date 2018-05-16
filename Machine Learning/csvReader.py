import csv

with open("/user/HS127/sc00858/OpenPose/Output/Train/Chew_dataset/datasetChew04.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))
