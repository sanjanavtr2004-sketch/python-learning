class students:
    def __init__(self, name, rollno, marks ): 
        self.name = name
        self.rollno = rollno
        self.marks = marks

    
    def result(self):
        print(f"my name is {self.name}, my roll no is {self.rollno}, my subject marks is {self.marks}")
        if self.marks > 45 and self.marks < 60:
            print("second devision",  "grade B",   "pass")
        else:
            print("first division",  "grade A",  "pass")

student_list = []     
def delete_contact():
    name = input("Please enter a name to delete: ")
    for i in student_list:
        if i["student_name"]==name:
            student_list.remove(i)
            print("student name delete successfully") 

            
        
# object criteria
s1 = students("sanjana",61,98)
s2 = students("monika",78,45)
s1.result()

s2.result()

student_list.append(s1)
student_list.append(s2)
print(student_list)
delete_contact()
print(student_list)





