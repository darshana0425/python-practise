Fullname = input("Enter your full name: (First name Last name as Jane Doe) ")
length = len(Fullname)
print (length)
Firstname = ""
Lastname = ""
flag = 0
for i in range(length):
    if flag == 0:
        if Fullname[i] == " ":
            i = i + 1
            flag = 1
            continue
        else:
            Firstname = Firstname + Fullname[i]
            i=i + 1
    else:
        Lastname = Lastname + Fullname[i]
        i = i + 1



print(f"Your name is: {Lastname} {Firstname}")

        