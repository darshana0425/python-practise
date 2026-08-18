#Author: Umesh Poudel
#Date: 28 July 2022
#Description: Program to read from a file

def main():
    # ...
    infile = open("students.txt", "r");
    # ... 
    print("{:10}{:10}{:20}{:20}".format("First","Last","City","Email"))
    print("{}".format("-"*60)) 

    # ...
    for line in infile:
        # ...
        student=line.split()
        
        # ...
        print(...)   
    # 
    infile.close()


main()
