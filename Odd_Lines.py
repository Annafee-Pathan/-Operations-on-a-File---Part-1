# Program to copy odd lines of one file to another

# open file in read mode
with open('Codingal.txt', 'r') as fn:
    lines = fn.readlines()

# open other file in write mode
with open('CodingalUpdated.txt', 'w') as fn1:
    for i in range(len(lines)):
        if i % 2 == 0:   # index starts from 0, so even index = odd line
            fn1.write(lines[i])

# read and display updated file content
with open('CodingalUpdated.txt', 'r') as fn1:
    print("Content of CodingalUpdated.txt (only odd lines):\n")
    print(fn1.read())
