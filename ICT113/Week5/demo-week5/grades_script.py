#Author: Umesh Poudel
#Date: 18 Aug 2023
#Description: Process grades using(file,loop,selection,string formating)

def process_grade(marks):
    grade=""
    if(marks>89):
       grade="HD"
    elif(marks>79):
       grade="D"
    elif(marks>69):
       grade="C"
    elif(marks>59):
       grade="P"
    else:
       grade="F" 

    return grade

def find_class_average(total,count):
    return total/count

def main():

    total=0
    count=0
    avg=0.0
    
    # open the file for reading 
    infile = open("grades.txt", "r");

    #print headings

    print("\n{:^55}\n".format("WIN Institute"))
    print("{:10}{:20}{:10}{:10}{:2}".format("ID","Name","Subject","Marks","Grade"))
    print("="*55)  

    #read the file a line at a time
    for line in infile:
        count=count + 1
        id,name,subject,marks=line.split(",")
        
        marks=int(marks) # convert marks(text) to int 
        total=total + marks
        grade=process_grade(marks)
        print("{:10}{:20}{:10}{:<10}{:2}".format(id,name,subject,marks,grade))

        
    print("="*55)
    avg=find_class_average(total,count)
    print("{:>40}{:5.2f}".format("Average: ",avg))

    # close the file
    infile.close()


main()
