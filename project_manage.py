# import database module
import random
import database
import csv
import sys
from database import Database, Readfile, Table

my_database = Database()

# define a function called initializing
def initializing():
    read1 = Readfile()
    person_csv = read1.read_file("persons.csv")
    login_csv = read1.read_file("login.csv")
    persons_table = database.Table('persons', person_csv)
    login_table = database.Table('login', login_csv)
    my_database.insert(persons_table)
    my_database.insert(login_table)
    project_table = Table('project_table', [])
    my_database.insert(project_table)
    advisor_pending_request = Table('advisor_pending_table', [])
    my_database.insert(advisor_pending_request)
    member_pending_request = Table('member_pending_table', [])
    my_database.insert(member_pending_request)

# define a funcion called login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    my_login = my_database.search("login").table
    for data in my_login:
        if data["username"] == username and data["password"] == password:
            return [data['ID'], data['role']]
        print("Wrong username or password")
        return None

# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python

# make calls to the initializing and login functions defined above

class Admin:
    def __init__(self, user_id):
        self.user_id = user_id

    def access(self):
        while True:
            print("admin access")
            print("1. View student")
            print("2. View project")
            print("3. Delete student")
            print("4. Add student")
            print("5.exit")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                for i in my_database.search('persons').table:
                    print(
                        f"ID: {i['ID']} Fullname: {i['fist']} {i['last']} Type: {i['type']}")
            elif user_input == 2:
                num_project = 1
                for i in my_database.search('project').table:
                    print(f'{num_project}. Title: {i["Title"]} Project: {i["ProjectID"]}')
                    num_project += 1
            elif user_input == 3:
                student_id = str(input("Enter Student ID: "))
                for i in my_database.search('persons').table:
                    if i['ID'] == student_id:
                        my_database.search('persons').table.pop(
                            my_database.search('persons').table.index(i))
                        print('Remove success')
            elif user_input == 4:
                new_student = {}
                new_student['ID'] = str(random.randint(1000000, 9999999))
                new_student['fist'] = input("Input Firstname: ")
                new_student['last'] = input("Input lastname: ")
                new_student['Type'] = input("Input Type: ")
                my_database.search('persons').table.append(new_student)
                print("Add success")
            elif user_input == 5:
                break
            else:
                print("invalid choice")


class Student:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name


    def see_request(self):
        view = my_database.search('member_pending')
        request = view.table.filter(lambda x: x['ID'] == self.user_id)
        print(request)

    def accept_decline(self):
        request_table = my_database.search('member_pending')
        project_table = my_database.search('project')
        project_inv_id = input("Enter the project ID: ")
        answer = input("Accept oe decline Y or N: ")
        print(request_table)

        if answer.lower() == 'y':
            for i in project_table.filter(lambda x: x['ProjectID'] == project_inv_id).table:
                if i['Member1'] == '-':
                    project_table.update('ProjectID', project_inv_id, 'Member1', '-', 'Member1', self.user_id)
                elif i['Member1'] != '-' and i['Member2'] == '-':
                    project_table.update('ProjectID', project_inv_id, 'Member2', '-', 'Member2', self.user_id)
                else:
                    print('This group is already full')
                break

    def create_project(self):
        project_title = input("Input your project name: ")
        project_id = random.randint(100000, 999999)
        create_proj = {'ProjectID': project_id,
                       'Title': project_title,
                       'Lead': self.user_id,
                       'Member1': " ",
                       'Member2': " ",
                       'Advisor': 'Waiting',
                       'Status': 'Processing'}
        project_table.insert(create_proj)



    def modify_project(self, project_id, new_title="", new_lead=""):
        project_table = my_database.search('project')
        project_table.update({'ProjectID': project_id, 'Title': new_title, 'Lead': new_lead})

    def access(self):
        while True:
            print("1. create project")
            print("2. view request")
            print("3.accept or deny request")
            print("4.Modify project")
            print("5.exit")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                self.create_project()
            if user_input == 2:
                self.see_request()
            if user_input == 3:
                self.accept_decline()
            if user_input == 4:
                project_id = input("Enter project id: ")
                new_title = input("Enter new title: ")
                new_lead = input("Enter new lead: ")
                self.modify_project(project_id, new_title, new_lead)
            if user_input == 5:
                break
            else:
                print("invalid choice")
class Lead(Student):
    def __init__(self, user_id, user_name, project_id):
        super().__init__(user_id, user_name)
        self.project_id = project_id

    def access(self):
        while True:
            print("1. view project")
            print("2. send invite")
            print("3.request for advisor")
            print("4.Modify project")
            print("4.submit project")
            print(".exit")





class Faculty:
    def __init__(self, user_id):
        self.user_id = user_id

    def accces(self):
        while True:
            print("1. check project request")
            print("2. evaluate project")
            user_input = int(input("Enter your choice: "))
            if user_input in (1, 2):
                return user_input
            else:
                print("invalid choice")

    # def access(self):
    #



















data = initializing()
val = login()
# login_table = data.search('login')
# person_table = data.search('persons')
# member_request = data.search('member_pending_request')
# advisor_request = data.search('advisor_pending_request')
project_table = data.search('project')

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
