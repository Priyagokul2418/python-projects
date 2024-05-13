details={}
def student():
 details={'name':name,'student_id':student_id,'GPA':GPA}
while True:
    print("\n1.add student\n2.Remove student\n3.update student\n4.display student details\n5.search student\n6.exit")
    choice=input("enter your choice : ")
    if choice=='1':
     name=input("Enter student name")
     student_id=input("enter student id")
     student_GPA=input("enter student GPA")
     details.update()
     details={'name':name,'student_id':student_id,'student_GPA':student_GPA}
     print(details)
    elif choice=='2':
     name=input("enter the name")
     details.pop('name')
     print("student has been removed")
    elif choice=='3':
     name=input("enter name")
     new_id=input("enter student id")
     new_GPA=input("enter new GPA")
     details.update()
    elif choice=='4':
      print("student details")
      print(details)
    elif choice=='5':
        found_name=input("enter the student to be found")
        if found_name==name:
            print("student name:",name)
            print("student id :",student_id)
            print("student GPA :",student_GPA)
        else:
            print("the student not found,please enter correct name")
     
    elif choice=='6':
       print("exit")
    else:
     print("enter correct value")
student()

             
            
     
     















            
