'''            Problem Statement:
Your task is to write a Python program that accomplishes the following:
First create a database , table and add these column 'student_id', 'first_name', 'last_name','age', 'grade'.
Connects to your MySQL database with python.
Inserts a new student record into the "students" table with the following details:
First Name: "Alice"
Last Name: "Smith"
Age: 18
Grade: 95.5
Updates the grade of the student with the first name "Alice" to 97.0.
Deletes the student with the last name "Smith."
Fetches and displays all student records from the "students" table. '''


import mysql.connector
mydb = mysql.connector.connect(host='localhost', password='Gopal123@#12345', user='root',database="mydatabase")
# mydb = mysql.connector.connect(host='localhost', password='Gopal123@#12345', user='root')

conn = mydb.cursor()


# # # creating database
# conn.execute("create database mydatabase")


# # creating table
conn.execute("create table student(student_id int, first_name varchar(20), last_name varchar(10), age int, grade float)")

# inserting new student
insert_query = "insert into student (student_id, first_name, last_name, age, grade) values (%s, %s, %s, %s, %s)"
insert_value = (1,"Alice", "Smith", 18, 95.5)

conn.execute(insert_query,insert_value)
mydb.commit()

# # updating the grade of alice
update_query = "update student set grade = %s where first_name = %s"
set_value = (97.0,"Alice")
conn.execute(update_query,set_value)
mydb.commit()

# # # Delete student with last_name
delete_student = "Delete from student where last_name = %s"
delete_data = ("Smith",)
conn.execute(delete_student, delete_data)
mydb.commit()

# # # fetches and display all student record
conn.execute('Select * from student')
conn.fetchall()

conn.close()
mydb.close()

