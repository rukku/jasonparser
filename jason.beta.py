import os
import csv
import time

#get all asc files for processing and dump them to a text file
def listAsc():
    ascList = open('asc.list.txt','wt')
    #ascList = []
    for r,d,f in os.walk("."):
        for files in f:
            if files.endswith(".asc"):
                print os.path.join(r,files) 
                out = os.path.join(r,files) + "\n" 
                ascList.write(out)
                #ascList.append(os.path.join(r,files))
    #return ascList

#Retrieves list of asc files from file for processing                
def readList():
    ascFile = open('asc.list.txt')
    ascList = []
    for line in ascFile.readlines():
        ascList.append(line)
        print line
        
    return ascList

#Formats date string
def getDate(stringdate):
    dateval = time.strptime(stringdate,"%d-%b-%Y")
    #print dateval
    #print time.strftime("%b-%Y", dateval)
    #return time.strftime("%b-%Y", dateval)
    #return str(dateval)
    return time.strftime("%d-%b-%Y", dateval)
    
def removeTime():
    pass
    
#Workhorse of the script
def process(asc):
    asc = asc[:-1]
    f = open(asc)
    print "Processing"+asc
    extension = '.txt'
    ycount = 0
    ytotal = 0.0
    subtotal = 0.0

    for line in f.readlines():
        if line.find("Equ_time")!=-1:
            dummy = line.split()
            yeardate = getDate(dummy[4][1:])
            year = yeardate[7:]
           
        elif line[0] =='#':
            continue
        else:
            entry = line.split()
            if entry[3] != 'NaN':
                ytotal = subtotal + float(entry[3])
                ycount += 1
            else:
                continue
            filename = year + extension
            if os.path.isfile(filename):
                g = open(filename, 'at')
            else:
                g = open(filename,'wt')
            
            #g.write(out)
            if len(line.split()) > 5:
                line = line[:-6] + "\n"
            #print filename
            g.write(yeardate+"  "+line[12:])
    
    
    f.close()
    if ycount!=0:
        g.close()
    g.close()

#process('./she/data/j2p0025c003.asc ')
#print os.getcwd()
if __name__ == "__main__":
    listAsc()
    ascList =readList()
    for line in ascList[:2]:
        process(line)
