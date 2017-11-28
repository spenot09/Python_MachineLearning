import os
import xlwt
import glob
import operator


# Create a workbook object
wb = xlwt.Workbook()
# Add a sheet object
ws = wb.add_sheet('Sheet1', cell_overwrite_ok=True)

x=0

linesFinal=[]

#,'08', '09', '10', '11','12', '16', '17','18', '19', '20', '21', '22', '23'
#files to loop through
fls=['12', '16', '17','18', '19', '20', '21', '22', '23']

for i in fls:
    rowy = 0

    fname= ("/user/HS127/sc00858/OpenPose/Output/MVI_00%s/NotChew_MVI_00%s" % (i, i))

    os.chdir(fname)

    for text_filename in glob.glob('*.json'):

        with open(text_filename) as f_input:
            try:
                lines = [line.strip() for line in operator.itemgetter(5, 8)(f_input.readlines())]
                temp = lines[0] + ', ' + lines[1] +', 0'
                linesFinal.append(temp)

            #if JSON file is in incorrect format catch IndexError that would occur
            except IndexError as e:
                #remove frames that are not needed
                 os.remove(fname+'/'+text_filename)
                 print ('removed')

        #split elements
        for element in linesFinal:
            mylist = element.split(',')

        #delete every confidence element
        del mylist[2::3]

        # Output to Excel sheet
        for colno, colitem in enumerate(mylist):
            ws.write(rowy, colno, colitem)
        rowy += 1

    os.chdir('/user/HS127/sc00858/OpenPose/Output/Train')
    wb.save('datasetNotChew%s.xls' % i)
