#PROJECTX — SHOP INVENTORY MANAGEMENT SYSTEM

#ProjectX is designed to make shop inventory management simpler, faster, and more organized. It allows users to
#add, search, update, delete, and view product records through 
#a menu-driven Python interface connected to a MySQL database.

#Manage your inventory efficiently, access product information easily, and keep your shop records organized.

#Developed by Sneh Keshari

#Happy Shopping! Happy Programming!

import mysql.connector as c

mydb = c.connect(
    host='localhost',
    user='root',
    passwd=input("Enter your MySQL password: "),
    database='Projectrec_1'
)
cur = mydb.cursor()


def Insertion():
    print("-----INSERTING THE VALUES-----")
    while True:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        cd = int(input("ENTER THE CODE NO :- "))
        itname = input("ENTER THE ITEM NAME :- ")
        itname2 = itname.upper()
        itsize = input("ENTER THE ITEM SIZE :- ")
        itqua = input("ENTER THE ITEM QUANTITY :- ")
        itprice = int(input("ENTER THE ITEM PRICE :- "))
        comp = input("ENTER THE COMPANY NAME :- ")
        comp2 = comp.upper()
        mobno = input("ENTER THE MOBILE NUMBER :- ")
        poo = input("ENTER THE PLACE OF ORIGIN :- ")
        poo2 = poo.upper()
        cur.execute(
            "Insert into goodsinfo values ({},'{}','{}','{}',{},'{}','{}','{}')".format(
                cd, itname2, itsize, itqua, itprice, comp2, mobno, poo2
            )
        )
        mydb.commit()
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        choice = int(input("ENTER 1 FOR MORE ENTRY\nENTER 2 FOR EXIT\nENTER YOUR CHOICE :- "))
        if choice == 2:
            break
    print("DATA INSERTED SUCCESSFULLY...")


def Delete():
    print("-----DELETING THE VALUES-----")
    cd1 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO DELETE THE RECORD :- "))
    cur.execute("select Code from goodsinfo")
    data = cur.fetchall()
    for i in data:
        if i[0] == cd1:
            print("RECHEAK YOUR CODE AGAIN WHICH YOU ENTERED ", cd1)
            DEL = input("READY TO DELETE PRESS [ 0 ]\nIF NOT PRESS ANY OTHER CHARACTER\nENTER YOUR CHOICE")
            
            if DEL == '0':
                cur.execute("DELETE FROM goodsinfo WHERE Code = ({})".format(cd1))
                mydb.commit()
                print("DATA DELETED SUCCESSFULLY...")
                break
            else:
                print("CHOSSE CHOICE AGAIN ")
                break
    else:
        print("CODE NOT FOUND ")


def UPDATEITPR():
    print("-----UPDATING THE VALUE FOR PRICE -----")
    cd2 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO UPDATE THE PRICE :- "))
    cur.execute("select Code from goodsinfo")
    data1 = cur.fetchall()
    for i in data1:
        if i[0] == cd2:
            UP2 = int(input("ENTER THE NEW PRICE FOR THE ITEM "))
            cur.execute(" UPDATE GOODSINFO SET Item_price = {} WHERE Code = {}".format(UP2, cd2))
            mydb.commit()
            print("PRICE UPDATED SUCCESSFULLY...")
            break
    else:
        print("CODE NOT FOUND ")


def UPDATECOMNAME():
    print("-----UPDATING THE VALUE FOR COMPANY NAME  -----")
    cd3 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO UPDATE THE COMPANY NAME :- "))
    cur.execute("select Code from goodsinfo")
    data1 = cur.fetchall()
    for i in data1:
        if i[0] == cd3:
            UP3 = input("ENTER THE NEW COMPANY NAME FOR THE ITEM ")
            cur.execute(" UPDATE GOODSINFO SET Company_name = '{}' WHERE Code= {}".format(UP3, cd3))
            mydb.commit()
            print("COMPANY NAME UPDATED SUCCESSFULLY...")
            break
    else:
        print("CODE NOT FOUND ")


def UPDATESIZE():
    print("-----UPDATING THE VALUE FOR SIZE  -----")
    cd4 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO UPDATE THE SIZE :- "))
    cur.execute("select Code from goodsinfo")
    data3 = cur.fetchall()
    for i in data3:
        if i[0] == cd4:
            UP4 = input("ENTER THE NEW SIZE FOR THE ITEM ")
            cur.execute(" UPDATE GOODSINFO SET Size = '{}' WHERE Code= {}".format(UP4, cd4))
            mydb.commit()
            print("SIZE UPDATED SUCCESSFULLY...")
            break
    else:
        print("CODE NOT FOUND ")


def UPDATEMONO():
    print("-----UPDATING THE VALUE FOR MOBILE NUMBER  -----")
    cd5 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO UPDATE THE MOBILE NUMBER :- "))
    cur.execute("select Code from goodsinfo")
    data4 = cur.fetchall()
    for i in data4:
        if i[0] == cd5:
            UP5 = input("ENTER THE NEW MOBILE NO FOR THE ITEM ")
            cur.execute(" UPDATE GOODSINFO SET Mobileno = '{}' WHERE Code= {}".format(UP5, cd5))
            mydb.commit()
            print("MOBILE NUMBER UPDATED SUCCESSFULLY...")
            break
    else:
        print("CODE NOT FOUND ")


def UPDATEITQUAN():
    print("-----UPDATING THE VALUE FOR ITEM QUANTITY-----")
    cd7 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO UPDATE THE QUANTITY :- "))
    cur.execute("select Code from goodsinfo")
    data6 = cur.fetchall()
    for i in data6:
        if i[0] == cd7:
            UP7 = input("ENTER THE NEW ITEM QUANTITY FOR THE ITEM ")
            cur.execute(" UPDATE GOODSINFO SET ITEM_QUANTITY = '{}' WHERE Code= {}".format(UP7, cd7))
            mydb.commit()
            print(" ITEM QUANTITY UPDATED SUCCESSFULLY...")
            break
    else:
        print("CODE NOT FOUND ")


def UPDATEITNAME():
    print("-----UPDATING THE VALUE FOR ITEM NAME-----")
    cd8 = int(input("ENTER THE CODE NO FOR WHICH YOU WANT TO UPDATE THE ITEM NAME :- "))
    cur.execute("select Code from goodsinfo")
    data7 = cur.fetchall()
    for i in data7:
        if i[0] == cd8:
            UP8 = input("ENTER THE NEW ITEM NAME FOR THE ITEM ")
            cur.execute(" UPDATE GOODSINFO SET ITEM_NAME = '{}' WHERE Code= {}".format(UP8, cd8))
            mydb.commit()
            print(" ITEM NAME UPDATED SUCCESSFULLY...")
            break
    else:
        print("CODE NOT FOUND ")


def VIEW():
    print("-----VIEWING THE DATA-----")
    give = input("GIVE THE ITEM NAME TO SEARCH")
    give2 = give.upper()
    cur.execute("select * from goodsinfo where Item_name like '%{}%' ".format(give2))
    data8 = cur.fetchall()
    if data8 == []:
        print('NO RECORD FOUND')
    else:
        print('C', 'It_name', 'Size', 'Item_qty', 'It_pric', 'Comp_name', 'Mobile_no', 'Place_of_origin')
        for i in data8:
            print(i)


def VIEWPRE():
    print("-----VIEWING THE DATA ONLY CODE ITNAME ITQUAN SIZE ITPRICE -----")
    give3 = input("GIVE THE ITEM NAME TO SEARCH")
    give4 = give3.upper()
    cur.execute("select Code,Item_name,Item_quantity,Size,Item_price from goodsinfo where Item_name like '%{}%' ".format(give4))
    data8 = cur.fetchall()
    if data8 == []:
        print('NO RECORD FOUND')
    else:
        print('C', 'It_name', 'Item_qty', 'Size', 'It_pric')
        for i in data8:
            print(i)


def VIEWbyplace():
    print("-----VIEWING THE DATA BY PLACE  -----")
    give4 = input("GIVE THE PLACE NAME TO SEARCH")
    give5 = give4.upper()
    cur.execute("select * from goodsinfo where PLACEOFORIGIN like '%{}%' ".format(give5))
    data9 = cur.fetchall()
    if data9 == []:
        print('NO RECORD FOUND')
    else:
        print('C', 'It_name', 'Size', 'Item_qty', 'It_pric', 'Comp_name', 'Mobile_no', 'Place_of_origin')
        for i in data9:
            print(i)


def VIEWbyCOMP():
    print("-----VIEWING THE DATA BY COMPANY NAME-----")
    give5 = input("GIVE THE COMPANY NAME TO SEARCH")
    give6 = give5.upper()
    cur.execute("select * from goodsinfo where Company_name like '%{}%' ".format(give6))
    data10 = cur.fetchall()
    if data10 == []:
        print('NO RECORD FOUND')
    else:
        print('C', 'It_name', 'Size', 'Item_qty', 'It_pric', 'Comp_name', 'Mobile_no', 'Place_of_origin')
        for i in data10:
            print(i)


def VIEWALL():
    print("-----VIEWING THE FULL TABLE OF RECORDS { MIGHT TAKE SOMETIME }-----")
    cur.execute("select * from goodsinfo ")
    data11 = cur.fetchall()
    if data11 == []:
        print('NO RECORD FOUND')
    else:
        print('C', 'It_name', 'Size', 'Item_qty', 'It_pric', 'Comp_name', 'Mobile_no', 'Place_of_origin')
        for i in data11:
            print(i)


# main
print("WELCOME TO PROJECTX GIVE YOUR QUERIES WILL BE DELIGHTEFULL TO HELP YOU ")
try:
    while True:
        CH = int(input(
            "PRESS\n 1 FOR SEARCH DATA\n 2 FOR SEARCH DATA ONLY ITNAME ,QTY, SIZE, PRICE"
            "\n 3 FOR search BY PLACE OF ORIGIN NAME\n 4 FOR search BY COMPANY-NAME"
            "\n 5 INSERT RECORDS INTO TABLE\n 6 UPDATE ITEM-PRICE\n 7 UPDATE ITEM QUANTITY"
            "\n 8  UPDATE COMPANY-NAME\n 9 UPDATE MOBILE NUMBER"
            "\n 11 UPDATE SIZE\n 12 UPDATE ITEM-NAME\n 13 VIEW THE FULL TABLE"
            "\n 14 DELETE A RECORD\n 15 EXIT FROM THE APPLICATION\nENTER YOUR CHOICE:-"
        ))
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        if CH == 1:
            VIEW()
        if CH == 2:
            VIEWPRE()
        if CH == 3:
            VIEWbyplace()
        if CH == 4:
            VIEWbyCOMP()
        if CH == 5:
            Insertion()
        if CH == 6:
            UPDATEITPR()
        if CH == 7:
            UPDATEITQUAN()
        if CH == 8:
            UPDATECOMNAME()
        if CH == 9:
            UPDATEMONO()
        #if CH == 10:
            #UPDATEpop()
        if CH == 11:
            UPDATESIZE()
        if CH == 12:
            UPDATEITNAME()
        if CH == 13:
            VIEWALL()
        if CH == 14:
            Delete()
        if CH == 15:
            break
        else:
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(" ENTER CHOICE AS NUMBERS BTWEEN 1 TO 15 ")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
except:
    print("ITS AN ERROR !! REASONS MAY BE:----- \n1. IT CAN BE FOR CHOICE :>ENTER THE CHOICE ONLY NUMBERS BETWEEN  1 TO 15>"
          "\n2.  IT CAN BE FOR GIVING CODE NO AS CHARCTER"
          "\n3. IT CAN BE GIVING PRICE AS CHARACTER  ")

mydb.commit()
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("APPLICIATION SESSION CAME TO AN END , IF YOU WANT AGAIN TO RUN THE APPLICATIONS THEN \nOPEN THE PROGRAM FILE (PROJECTX.py) AGAIN AND PRESS [F1]")
print("DESIGNED  BY SNEH KESHARI\nMAIL FOR ANY UPDATES AND CORRECTION AT :- kesharisneh25@gmail.com")
print("HAPPY SHOPING\nHAPPY PROGRAMING")
mydb.commit()
