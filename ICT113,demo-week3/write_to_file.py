#Author: Umesh Poudel
#Date: 28 July 2022
#Description: Program to write to a  text file

def main():
    # open the file for writing
    filename='python.txt'
    outfile = open(filename, 'w');

    #multiline string
    text="""
        What can Python do?

        Python can be used on a server to create web applications.
        Python can be used alongside software to create workflows.
        Python can connect to database systems. It can also read and modify files.
        Python can be used to handle big data and perform complex mathematics.
        Python can be used for rapid prototyping, or for production-ready software development.
    """
    
    # write the string myStr to the file.
    outfile.write(text);

    #close the file.
    outfile.close();

    print("File saved :",filename)

main()
