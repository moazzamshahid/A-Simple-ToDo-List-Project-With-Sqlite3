import re
from utils import create_table,add_task_db,get_all_tasks,delete_task_db,update_task_db,mark_task_complete_db


CHOICE="""
'a' for add Task in the List
'u' for update Task in the List
'l' for show list of Task
'd' for delete Task in the List
'c' for marking as complete
'q' for quit the program
"""
task_priority=["High","Medium","Low"]

def add_Task():
    Title=input("Add Title: ")
    Description=input("Add Description: ")
    priority=input("Add Prioriry [High, Medium, Low]: ")
    if priority not in task_priority:
        print("invalid Priority")
        return 0
    Due_DT=input("Add Due Date Time format ( x/x/xxxx xx:xx ): ")
    r = re.compile('\d{2}/\d{2}/\d{4} \d{2}:\d{2}')
    
    if r.match(Due_DT) is None:
        print("not matching")
        return 0

    add_task_db(Title=Title,Description=Description,priority=priority,Due_Date=Due_DT)
#-----------------------------------------------------------
def delete_task():
    Title=input("Add Title: ")
    delete_task_db(Title=Title)
    
    
#-----------------------------------------------------------

def update_task():
    Title=input("Enter Title: ")
    option=input("Enter 'd' for Due Date Change and 'p' for priority change: ")
    if option =='d':
        Due_DT=input("Add Due Date Time format ( x/x/xxxx xx:xx ): ")
        r = re.compile('\d{2}/\d{2}/\d{4} \d{2}:\d{2}')
        if r.match(Due_DT) is not None:
            update_task_db(Title=Title,option=option,value=Due_DT)
        else: 
            print("wrong format")
    elif option == 'p':
        print("change priority")
        priority=input("Add Prioriry [High, Medium, Low]: ")
        if priority in task_priority:
            update_task_db(Title=Title,option=option,value=priority)
        else:
            print("invalid Priority")
    else:
        print("wrong option ! try again")

def mark_task_complete():
    Title=input("Enter Title: ")
    mark_task_complete_db(Title)

def display_all_tasks():
    get_all_tasks()

opertion={
    'a':add_Task,
    'u':update_task,
    'd':delete_task,
    'c':mark_task_complete,
    'l':display_all_tasks

}


def menu():
    option=input(CHOICE)
    while option != 'q':
        try:
            function=opertion[option]
            function()
        except KeyError:
            print("invalid Option, Please try again")

        option=input(CHOICE)



if __name__=="__main__":
    create_table()
    menu()










    
