import pymysql
import sys

def connect():
    global cursor, con
    try:
        con = pymysql.connect(host='localhost',user='root',password='',database='test')
    except pymysql.Error as e:
        print(e,'not connnected to server')
        sys.exit(0)
    print('connected to server')

    cursor = con.cursor()

def crclose():
    cursor.close()
    con.close()
    print('connection closed')


def createTable():
    connect()
    query = '''create table ANGEL(username varchar(20) primary key,password varchar(20), name varchar(20), dob varchar(10))'''
    try:
        cursor.execute(query)
        print('table created succesfully')
        return True
    except pymysql.Error as e:
        e = str(e)
        if 'already exists' in e:
            return True
        print(e)


def drop_table():
    connect()
    sql = "DROP TABLE ANGEL"

    # execute the SQL statement
    cursor.execute(sql)
    print('table deleted')

    # commit the changes to the database
    con.commit()
    crclose()

def singup(use,pas,name,dob):
    connect()
    try:
        query = '''select * from ANGEL where username=%s'''
        info = use
        cursor.execute(query,info)
        data = cursor.fetchone()
        if not data:
            query = '''insert into ANGEL values(%s,%s,%s,%s)'''
            info = (info, pas,name,dob)
            cursor.execute(query,info)
            con.commit()
            print('Account created succesfully')
            return 1
        else:
            print('User already exist')
            return 2
        
    except pymysql.Error as e:
        print(e,'singup')


def singin(use,pas):
    connect()
    try:
        query = '''select * from ANGEL where username=%s or password = %s'''
        info = (use,pas)
        cursor.execute(query,info)
        data = cursor.fetchone()
        if data and info[0]==data[0]:
            if data[1]==info[1]:
                print('login succesfull')
                crclose()
                return 1
            else:
                print('invalid password')
                crclose()
                return 2
        else:
                print("Username not found please Sing Up")
                crclose()
                return 3
    except pymysql.Error as e:
        print(e,'singin')


def forgot(use,dob,new=''):
    connect()
    try:
        query = '''select * from ANGEL where username=%s or dob=%s'''
        info = (use,dob)
        cursor.execute(query,info)
        data = cursor.fetchone()

        if data and info[0] == data[0]:
            if data[3]==info[1]:
                query = '''UPDATE ANGEL SET password = %s WHERE username=%s'''
                info = (new,use)
                cursor.execute(query,info)
                con.commit()
                print('password changed succesfully...')
                crclose()
                return 1

            else:
                print('invalid credentials')
                crclose()
                return 2

        else:
            print("Username not found please Sing Up")
            crclose()
            return 3

    except pymysql.Error as e:
        print(e,'forgot')

