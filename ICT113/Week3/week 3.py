
def man():
    a= "My_Name"
    for i in range(len(a)):
        print(a[i])


def abc():
    import math
    a= math.sqrt(81)
    print (a)


# program to read and display a text file
def main():
    # open the file for reading
    infile = open("ICT113/Week3/students.txt", "r")    #read the file a line at a time
    for line in infile:
        # display the line
        print (line)
    # close the file
    infile.close()
    print ('a' not in "basd")

main()

import math 

abc = int(input("Enter a no")) 

square_root= f"{math.sqrt(abc):.1f}" 

  

print(square_root) 


    
        
