from unittest import result
from .database_connection import Database_Connection



def create_table():
    with Database_Connection("data.db") as cursor:
       # cursor=connection.cursor()
        cursor.execute("create Table if not exists To_Do_List(T_no INTEGER PRIMARY KEY AUTOINCREMENT,Title text , Description text,priority text, Due_Date_time text, Status text)")



def add_task_db(Title,Description,priority,Due_Date):
    with Database_Connection("data.db") as cursor:
        status="Pending"
        cursor.execute("INSERT INTO To_Do_List(Title,Description,priority,Due_Date_time,Status) VALUES(?,?,?,?,?)",(Title,Description,priority,Due_Date,status))

def get_all_tasks():
    with Database_Connection("data.db") as cursor:
        result=cursor.execute("SELECT * FROM To_Do_List")
        print(result.fetchall())
    
def delete_task_db(Title):
    with Database_Connection("data.db") as cursor:
        cursor.execute("DELETE FROM To_Do_List where Title=?",(Title,))

def update_task_db(Title,option,value):
    with Database_Connection("data.db") as cursor:

        if option=='d':
            cursor.execute("UPDATE To_Do_List SET Due_Date_time=? where Title=?",(value,Title))  
        elif option=='p':
            print("In priority change")
            cursor.execute("UPDATE To_Do_List SET priority=? where Title=?",(value,Title))

def mark_task_complete_db(Title):
    with Database_Connection("data.db") as cursor:
        cursor.execute("UPDATE To_Do_List SET Status='Complete' where Title=?",(Title,))


