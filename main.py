def choice1():
    courses=open("courses.txt","r+",encoding="utf-8")
    for aline in courses:
        values=aline.split(";",2)
        print(values[0],values[1])
    courses.close()

def choice2():
    courses = open("courses.txt", "r+", encoding="utf-8")
    for aline in courses:
        values = aline.split(";", 3)
        studentnumber=int(values[3])
        if studentnumber>0:
            print(values[0], values[1])
    courses.close()

def choice3():
    coursename=input("Please enter a course name that you want to add:")
    coursecode=input("Please enter a course code that you want to add:")
    courseinstructor=input("Please enter a course instructor that you want to add:")
    list3=[coursecode,coursename,courseinstructor]
    courses = open("courses.txt", "a", encoding="utf-8")
    courses.write("\n")
    for appending in list3:
        courses.write(appending)
        courses.write(";")
    courses.close()

def choice4():
    findingcode=input("Please enter a course code that you want to search:")
    courses = open("courses.txt", "r", encoding="utf-8")
    for aline in courses:
        line=0
        values=aline.split(";",3)
        if findingcode==values[line]:
            print(values[0],values[1],values[2])
        line=line+1
    courses.close()

def choice5():
    findingname=input("Please enter a course name that you want to search:")
    courses = open("courses.txt", "r", encoding="utf-8")
    for aline in courses:
        line=0
        values=aline.split(";",3)
        if findingname in values[1]:
            print(values[0],values[1],values[2])
        line=line+1
    courses.close()

def choice6():
    deletecomma = 0
    newid = input("Please enter a new student's id:")
    newstudent = input("Please enter a new student's name:")
    newscoursecode = input("Please enter a new student's course code(If you want to add more than one,please use comma):")
    list6 = [newid, newstudent, newscoursecode]
    students = open("students.txt", "a", encoding="utf-8")
    students.write("\n")
    for appendingstudents in list6:
        students.write(appendingstudents)
        if deletecomma < 2:
            students.write(";")
        deletecomma = deletecomma + 1

    # courses = open("courses.txt", encoding="utf-8")
    # mylines = []
    # for line_of_text in courses:
    #     mylines.append(line_of_text.strip("\n"))
    #     liste = mylines
    # print(liste)
    # courses.close()
    # y=0
    # for aline in liste:
    #     values=aline.split(";")
    #     if newscoursecode in liste[y]:
    #         eskisayi=values[3]
    #         liste[y].pop()
    #         liste[y].append(int(eskisayi)+1)
    #         y=y+1
    #     else:
    #         y=y+1
    # print(liste)
    students.close()


def choice7():
    students = open("students.txt", "r", encoding="utf-8")
    for aline in students:
        values = aline.split(";", 3)
        print(values[1],":",values[2])
    students.close()


def choice8():
    courses = open("courses.txt", "r", encoding="utf-8")
    newlist=[]
    for aline in courses:
        values=aline.split(";")
        newlist.append(values[3]+" "+values[1])
        newlist.sort(reverse=True)
    new_list = [item.replace('\r', '').replace('\n', '') for item in newlist]
    abc=0
    y=-3
    while y:
        if new_list[abc]==new_list[abc+1]:
            print(new_list[abc])
            print(new_list[abc+1])
            abc=abc+1
            y=y+1
        else:
            print(new_list[abc])
            abc=abc+1
            y=y+1
    courses.close()

def choice9():
    students = open("students.txt", "r", encoding="utf-8")
    coursesnumbers=[]
    studentnames=[]
    for aline in students:
        values=aline.split(";")
        tekrar=values[2].count("CENG")
        coursesnumbers.append(tekrar)
        studentnames.append(values[1])
    for i in range(3):
        index1=int(coursesnumbers.index(max(coursesnumbers)))
        print(coursesnumbers[index1],end="")
        print(" ",studentnames[index1])
        coursesnumbers[index1]=0
    students.close()


y=1
while y:
    name=input("Please enter your Name:").upper()
    surname=input("Please enter your Surname:").upper()
    if (name!="OZAN" or surname!="USLAN"):
        print("Wrong admin information! Please try again")
    else:
        break
print("---Welcome",name,surname,"---")

button=0
liste=[]
print("\nPlease choose an option that what do you want to. You can go previous or next by 'Previous' and 'Next'")
for i in ("exit the menu.","list all courses.","list all courses that have at least 1 student.","add new course.","search a course depend on it's code.","searc a course depend on it's name.","register a student to a course.","list all the students their registered courses.","list top 3 most crowded courses.","list top 3 students with the most course registrations."):
    print("-Enter",button,"to",i)
    liste.append(button)
    button=button+1

x=1
while x:
    choice = int(input("\n\nPlease enter your choice:\n"))
    if choice not in liste:
        print("Invalid number")
    else:
        if choice==0:
            break
        elif choice==1:
            choice1()
        elif choice==2:
            choice2()
        elif choice==3:
            choice3()
        elif choice==4:
            choice4()
        elif choice==5:
            choice5()
        elif choice==6:
            choice6()
        elif choice==7:
            choice7()
        elif choice==8:
            choice8()
        elif choice==9:
            choice9()