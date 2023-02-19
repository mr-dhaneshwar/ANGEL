import pymysql
import sys

try:
    con = pymysql.connect(host='localhost',user='root',password='',database='test')
except pymysql.Error as e:
    print(e,'not connnected')
    sys.exit(0)
print('connected')

cursor = con.cursor()
def createTable():
    query = '''create table ANGEL(username varchar(20) primary key,password varchar(20))'''
    try:
        cursor.execute(query)
        return True
    except pymysql.Error as e:
        e = str(e)
        if 'already exists' in e:
            return True
        print(e)
if createTable():
    def singup():
        try:
            query = '''select * from ANGEL where username=%s'''
            info = input('enter username: ')
            cursor.execute(query,info)
            data = cursor.fetchone()
            if data:
                print('user already exist')
            else:
                query = '''insert into ANGEL values(%s,%s)'''
                info = (input('enter username: '),input('enter password: '))
                cursor.execute(query,info)
                con.commit()
                print('Account created succesfully')
        except pymysql.Error as e:
            print(e,'singup')
    def singin():
        try:
            query = '''select * from ANGEL where username=%s or password = %s'''
            info = (input('enter username: '),input('enter password: '))
            cursor.execute(query,info)
            data = cursor.fetchone()
            if data and info[0]==data[0]:
                if data[1]==info[1]:
                    print('login succesfull')
                else:
                    print('invalid password')
            else:
                 print("Username not found please create an account")
                 singup()
        except pymysql.Error as e:
            print(e,'singin')
    singup()
    singin()
    cursor.close()
    con.close()