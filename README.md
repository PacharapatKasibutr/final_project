## How to use
* run project_manage

## description
* class Admin
  - view student
  - view project
  - delete student
  - add student
* class Student
  - create project
  - view request
  - accept or deny request
  - modify project
* class Lead
  - view project
  - sent invite
  - request for advisor
  - modify project
  - submit project
* class Member
  - view project
  - modify project
* class Faculty
  - check project request
  - view project
  - evaluate project
* class Advisor
  - check project request
  - view project
  - evaluate project
  - response
## completion percentage
|  Role   |                    Action                     |           Method           |      Class      | Completion percentage |
|:-------:|:---------------------------------------------:|:--------------------------:|:---------------:|:---------------------:|
|  Admin  |    view student,project add,delete student    |           access           |      Admin      |         100%          |
| Student |                  see request                  |        see_request         |     Student     |         100%          |
| Student |         acceept or decline invitation         |       accept_decline       |     Student     |          80%          |
| Student |                create project                 |       create_project       |     Student     |          90%          |
| Student |                Check requests                 |        read_request        |     Student     |         100%          |
| Student |                modify project                 |       modify_project       |     Student     |          80%          |
| Student |         access to different function          |           access           |     Student     |         100%          |
|  Lead   |                 view project                  |        view_project        |      Lead       |          90%          |
|  Lead   |         send invitation for member            |       send_invitation      |      Lead       |          80%          |
|  Lead   |            request for advisor                |      request_advisor       |      Lead       |          90%          |
|  Lead   |               submit project                  |       submit_project       |      Lead       |          90%          |
|  Lead   |         access to different function          |           access           |      Lead       |         100%          |
|  Member |                 view project                  |        view_project        |      Member     |          90%          |
|  Member |         access to different function          |           access           |      Member     |         100%          |
| Faculty |                 view project                  |        view_project        |     Faculty     |          90%          |
| Faculty |                 check request                 |       check_request        |     Faculty     |          80%          |
| Faculty |          Evaluated assigned projects          |      evaluate_project      |     Faculty     |          80%          |
| Faculty |         access to different function          |           access           |     Faculty     |         100%          |
| Advisor |                   response                    |          response          |     Advisor     |          90%          |
| Advisor |         access to different function          |           access           |     Advisor     |         100%          |


## missing feature and bug
* missing some admin command such as update tabow for admin and insert row
* some of the function doesn't seem to work 
