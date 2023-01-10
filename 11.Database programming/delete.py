'''
Delete record from database table

sql query for deleting record:
---------------------------

delte from tablename where id=value


where id=value               =>Serach

delete from tablename        =>delete that record

'''




import pymysql

try:
    db=pymysql.connect(host="localhost", user="root", password="", database="company")
    cu=db.cursor()
    q="delete from employee where id=2"
    cu.execute(q)
    db.commit()

    
    print("Deleting Record Successfully")

except Exception as e:
    print("Error:",e)
