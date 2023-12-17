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
    persons_table = database.Table('persons', person_csv)
    my_database.insert(persons_table)

    login_csv = read1.read_file("login.csv")
    login_table = database.Table('login', login_csv)
    my_database.insert(login_table)

    advisor_pending_csv = read1.read_file("advisor_pending_request.csv")
    advisor_pending_request_table = database.Table('advisor_pending_request', advisor_pending_csv)
    my_database.insert(advisor_pending_request_table)

    member_pending_csv = read1.read_file("member_pending_request.csv")
    member_pending_request_table = database.Table('member_pending_request', member_pending_csv)
    my_database.insert(member_pending_request_table)

    project_csv = read1.read_file("project.csv")
    project_table = database.Table('project', project_csv)
    my_database.insert(project_table)

# define a function called login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    my_login = my_database.search("login").table
    for data in my_login:
        if data["username"] == username and data["password"] == password:
            return [data['ID'], data['role']]
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
    def __init__(self, user_id, user_first, user_last):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last

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
                for project in my_database.search('project').table:
                    print(f"Project ID: {project['ProjectID']}")
                    print(f"Title: {project['Title']}")
                    print(f"Lead: {project['Lead']}")
                    print(f"Member1: {project['Member1']}")
                    print(f"Member2: {project['Member2']}")
                    print(f"Advisor: {project['Advisor']}")
                    print(f"Status: {project['Status']}")
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
    def __init__(self, user_id, user_first, user_last):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last


    def see_request(self):
        view = my_database.search('member_pending')
        request = view.table.filter(lambda x: x['ID'] == self.user_id)
        print(request)

    def accept_decline(self):
        request_table = my_database.search('member_pending')
        project_table = my_database.search('project')
        project_inv_id = input("Enter the project ID: ")
        answer = input("Accept or decline Y or N: ")
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
            print("1.create project")
            print("2.view request")
            print("3.accept or deny request")
            print("4.Modify project")
            print("5.exit")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                my_database.search('login').update('ID', self.user_id, 'role', 'lead')
                self.create_project()
            elif user_input == 2:
                self.see_request()
            elif user_input == 3:
                self.accept_decline()
            elif user_input == 4:
                project_id = input("Enter project id: ")
                new_title = input("Enter new title: ")
                new_lead = input("Enter new lead: ")
                self.modify_project(project_id, new_title, new_lead)
            elif user_input == 5:
                break
            else:
                print("invalid choice")
class Lead(Student):
    def __init__(self, user_id, user_first, user_last, project_id):
        super().__init__(user_id, user_first, user_last)
        self.project_id = project_id

    def view_project(self):
        view_pro = project_table
        for project in view_pro:
            print(f"ProjectID: {project['ProjectID']}")
            print(f"Title: {project['Title']}")
            print(f"Lead: {project['Lead']}")
            print(f"Member1: {project['Member1']}")
            print(f"Member2: {project['Member2']}")
            print(f"Advisor: {project['Advisor']}")
            print(f"Status: {project['Status']}")
    def send_invitation(self):
        invite = input("Enter student ID for invitation: ")
        member_request_table = my_database.search('member_pending_request')
        if member_request_table:
            member_request_table.insert({'ProjectID': self.project_id, 'to_be_member': invite})
        else:
            print("Wrong ID!")

    def request_advisor(self):
        advisor = input("Enter advisor ID: ")
        advisor_request_table = my_database.search('advisor_pending_request')
        if advisor_request_table:
            advisor_request_table.insert({'ProjectID': self.project_id, 'to_be_member': advisor})

    def submit_project(self):
        submit = input("Submitting project y or no: ")
        if submit.lower() == "y":
            project_table = my_database.search('project')
            if project_table:
                project_table.insert({'ProjectID': self.project_id, 'Status': "submitted"})
        else:
            print("cancel")



    def access(self):
        while True:
            print("1.view project")
            print("2.send invite")
            print("3.request for advisor")
            print("4.Modify project")
            print("5.submit project")
            print("6.exit")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                self.view_project()
            elif user_input == 2:
                self.send_invitation()
            elif user_input == 3:
                self.request_advisor()
            elif user_input == 4:
                project_id = input("Enter project id: ")
                new_title = input("Enter new title: ")
                new_lead = input("Enter new lead: ")
                self.modify_project(project_id, new_title, new_lead)
            elif user_input == 5:
                self.submit_project()
            elif user_input == 6:
                break
            else:
                print("invalid choice")


class Member(Student):
    def __init__(self, user_id, user_name, project_id):
        super().__init__(user_id, user_name)
        self.project_id = project_id

    def view_project(self):
        view_pro = project_table
        for project in view_pro:
            print(f"ProjectID: {project['ProjectID']}")
            print(f"Title: {project['Title']}")
            print(f"Lead: {project['Lead']}")
            print(f"Member1: {project['Member1']}")
            print(f"Member2: {project['Member2']}")
            print(f"Advisor: {project['Advisor']}")
            print(f"Status: {project['Status']}")
    def access(self):
        while True:
            print("1. View Project")
            print("2. Modify Project")
            print("3.exit")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                self.view_project()
            elif user_input == 2:
                project_id = input("Enter project id: ")
                new_title = input("Enter new title: ")
                new_lead = input("Enter new lead: ")
                self.modify_project(project_id, new_title, new_lead)
            elif user_input == 3:
                break
            else:
                print("invalid choice")



class Faculty:
    def __init__(self, user_id, user_first, user_last):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last

    def accces(self):
        while True:
            print("1.check project request")
            print("2.view project")
            print("3.evaluate project")
            print("4.exit")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                pass
            elif user_input == 2:
                self.view_project()
            elif user_input == 3:
                pass
            elif user_input == 4:
                pass
            else:
                print("invalid choice")

    # def access(self):
    #


class Advisor:
    pass















initializing()
val = login()
project_table = my_database.search('project')
# login_table = my_database.search('login')
# person_table = my_database.search('persons')
# member_request = my_database.search('member_pending_request')
# advisor_request = my_database.search('advisor_pending_request')

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
