#Author: Umesh Poudel
#Date: 28 July 2022
#Description: Program to read from a file

def main():
    # open the file for reading 
    infile = open("students.txt", "r");

    #read the file a line at a time
    for line in infile:
        # String line is split into a List 
        student=line.split()
        
        # display the line
        print(student[0]," lives in ",student[2])   

    # close the file
    infile.close()


main()
