#!/usr/bin/env python3
import os
# set the directory, the outfile and the tag below
dr = "/user/HS127/sc00858/OpenPose/Output"; out = "/user/HS127/sc00858/OpenPose/Code/Outputpy"; tag = ".json"

for f in [f for f in os.listdir(dr) if f.endswith(".json")]:
    open(out, "+a").write(("").join([l for l in open(dr+"/"+f).readlines()[4:6]])+"\n")
    open(out, "+a").write(("").join([l for l in open(dr+"/"+f).readlines()[7:9]])+"\n")
    open(out, "+a").write(("").join([l for l in open(dr+"/"+f).readlines()[10:12]])+"\n")
    open(out, "+a").write(("").join([l for l in open(dr+"/"+f).readlines()[13:15]])+"\n")


    #!/usr/bin/env python3
