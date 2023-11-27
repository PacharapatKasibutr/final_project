# import database module
import database
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
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    my_login = my_database.search("login")
    my_user = my_login.table
    for data in my_user:
        if data["ID"] == username and data["password"] == password:
            print(f"Hello {data['username']}")
            print(f"Permission level: {data['role']}")
            return data


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

initializing()
val = login()

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
