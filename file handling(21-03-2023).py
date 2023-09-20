#Write a program to get roll no,name,and marks from user and save records in a file 



#Writng list contents in a file
fileout=open("chintu.txt","a")
lst=[]

for i in range(5):
    name=input("Entera student name")
    lst.append(name)
    lst.append("\n")

#print(lst)
fileout.writelines(lst)
fileout.close()


