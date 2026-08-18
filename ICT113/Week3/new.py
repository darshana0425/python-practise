def main():
    # open the file for reading
    infile = open("students.txt", "r")    #read the file a line at a time
    for line in infile:
        # display the line
        print (line)
    # close the file
    infile.close()


main()
