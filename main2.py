file=open('file.txt','r')
print("Rading first line...")
print(file.readline())
file.close()

print("---------------------------------------")

file=open('file.txt','r')
print("Rading multiple line...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("---------------------------------------")

file=open('file.txt','r')
print("Looping through the lines")
for line in file:
    print(line)
file.close()