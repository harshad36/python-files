'''
Updateing a specific record
===========================

Harry =>Hari  It=> CS   70000 => 20000

SQL querry for update a record:
----------------------------

update tablename set colname1= newval1,colname2=val2, colname3=newval3....n where id=value


In update is done two steps
1) Search a record => where id value
2) update record  => set col1=newvalue1,col2=newvalue2,.....coln=newvaluen
'''



import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="",database="company")
    cu=db.cursor()
    q="update employee set name='hari',dept='CS',sal='20000' where id=1"
    cu.execute(q)
    db.commit()
    print("Record Updated Successfully")
except Exception as e:
    print("Error:",e)
