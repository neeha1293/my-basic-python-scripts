# simple script to merge 2 files based on date and time for correlating timing of events
#INSTRUCTIONS:
# Paste this script in the same folder as your two source files, otherwise you have to modify the path in the code

from datetime import datetime
import re, os

## LOGIC: use datetime module to directly do math on dates.
## for sorting, use simple 2 pointer

def parsefile(file): #from txt file to list datatype
    log = []
    path = os.path.join(os.path.abspath('.'),file) 
    f = open(path,'r')
    log = f.readlines()
    return log

def parsetimestamp(logline):

    regex = re.compile(r'\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}')

    if regex.search(logline) != None:
        return regex.search(logline).group()

    return None


def merge(file1, file2):

    list = []
    p1 = 0
    p2 = 0

    log1 = parsefile(file1)
    log2 = parsefile(file2)

    while p1 < len(log1) and p2 < len(log2):
        time1 = parsetimestamp(log1[p1])
        time2 = parsetimestamp(log2[p2])

        t1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")

        if t1<t2:
            list.append(log1[p1])
            p1 += 1
        else:
            list.append(log2[p2])
            p2 += 1

    return list
  
## MAIN   
log1 = input("enter first filename ex:log1.txt")
log2 = input("enter second filename ex:log2.txt")
mergedlogs = merge(log1,log2)

path = os.path.join(os.path.abspath('.'),'mergedlogs.txt')
newfile = open(path,'w')
for log in mergedlogs:
    newfile.write(log)

print("Merged file created: mergedlogs.txt")
