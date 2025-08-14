file1=open('file.txt','r')
file2=open('fileupd.txt','w')
for line in file1.readlines():
    if not (line.startswith('They')):
        print(line)
        file2.write(line)
file2.close()
file1.close()