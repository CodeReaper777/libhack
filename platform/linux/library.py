import os
import random
import mysql.connector
import datetime
from getpass import getpass
from prettytable import PrettyTable
from rich.console import Console
from tqdm import tqdm
from rich.style import Style
from rich import print
from time import sleep
cuuruser = []
console = Console()
time = datetime.date.today()
db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="library"
    )
mycrc = db.cursor()

def processing():
    for _ in tqdm(range(100),desc="Processing",colour="cyan",mininterval= 0.02):
               sleep(0.01)
base = Style.parse("cyan")
class administrator:
    def CE_addBooks(self,name,author,publisher,price,status,year):
        try:
            if status == "avaliable" or status == "issued":
                rand = random.randint(1000,4000)
                mycrc.execute("INSERT INTO ce_books(books,author,Book_code,publisher,price,Status,year) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,author,rand,publisher,price,status,year))
                db.commit()
                print(f"\n\nBook added to the List successfully at {time}")  
                input("Press Enter to continue...")
            else:
                print("[bold red]ERROR: Invalid Input...[/bold red]")
                input("Press Enter to continue...")
        except ValueError:
            print("[bold red]ERROR: Invalid Input...[/bold red]")
        os.system("clear")
    
    def CSE_addBooks(self,name,author,publisher,price,status,year):
        try:
            if status == "avaliable" or status == "issued":
                rand = random.randint(5000,9000)
                mycrc.execute("INSERT INTO cse_books(books,author,Book_code,publisher,price,Status,year) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,author,rand,publisher,price,status,year))
                db.commit()
                print(f"\n\nBook added to the List successfully at {time}")  
                input("Press Enter to continue...")
            else:
                print("[bold red]ERROR: Invalid Input...[/bold red]")
                input("Press Enter to continue...")
        except ValueError:
            print("[bold red]ERROR: Invalid Input...[/bold red]")
        os.system("clear")
    
    def CE_display(self,cyear):
            dbTable = PrettyTable()
            console.print("------------------Computer Enginnering------------------",style="bold cyan")
            mycrc.execute(f"SELECT books,author,Book_code,publisher,price,status from ce_books where year = {cyear}")
            dbTable.field_names = [ "Books", "Author","Book Code","Publicher", "Price","Status"]
            for data in mycrc:
                dbTable.add_row(data)
            print(dbTable)
            db.commit()
    
    def CSE_display(self,cyear):
            dbTable = PrettyTable()
            console.print("\t\t\n------------------Computer Science & Enginnering------------------",style="bold cyan")
            mycrc.execute(f"SELECT books,author,Book_code,publisher,price,status from cse_books where year = {cyear}")
            dbTable.field_names = ["Books", "Author","Book Code","Publicher", "Price","Status"]
            for data1 in mycrc:
                dbTable.add_row(data1)
            print(dbTable)
            db.commit()
            
    
    def showissued(self):
            console.print("--------------------------Issued Books-----------------------------",style="bold cyan")
            mycrc.execute("select * from issue_book")
            dbtables = PrettyTable()
            dbtables.field_names = ["Book Code","Book","ID","Student Name"]
            for x in mycrc:
                dbtables.add_row(x)
            print(dbtables)
            db.commit()
            

    def yearTable(self,year):
        temp = year
        stud = student()
        try:
            os.system("clear")
            submenu = ('''
                [bold green]+-----------+--------------+---------------------------------------+[/bold green ]
                [bold green]|[bold cyan]   Sr.no[/bold cyan]   | [bold cyan]Branch Code[/bold cyan]  |[/bold green][bold cyan]                  Trade                [/bold cyan][bold green]|[/bold green]
                [bold green]+-----------+--------------+---------------------------------------+[/bold green]
                [bold green]|[/bold green]     1.    [bold green]|[/bold green][bold cyan]    SE        [/bold cyan][bold green]|[/bold green][bold cyan] Second Year(SE)[/bold cyan]                    [bold green]   |[/bold green]
                [bold green]|[/bold green]     2.    [bold green]|[/bold green][bold cyan]    TE        [/bold cyan][bold green]|[/bold green][bold cyan] Third Year(TE)[/bold cyan]                     [bold green]   |[/bold green]
                [bold green]|[/bold green]     3.    [bold green]|[/bold green][bold cyan]    FE        [/bold cyan][bold green]|[/bold green][bold cyan] Fourth Year(FE)[/bold cyan]                    [bold green]   |[/bold green]
                [bold green]|[/bold green]     4.    [bold green]|[/bold green][bold cyan]     -        [/bold cyan][bold green]|[/bold green][bold cyan] Back To Menu[/bold cyan]                       [bold green]   |[/bold green]
                [bold green]+-----------+--------------+---------------------------------------+[/bold green]''')
            print(submenu)
            ch = int(input("\t\t ~ Enter: "))
            os.system("clear")
            if(year == 1):
                if(ch == 1):
                    self.CE_display(2)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return self.showTable()
                elif (ch == 2):
                    self.CE_display(3)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return self.showTable()
                elif (ch == 3):
                    self.CE_display(4)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return self.showTable()
                elif (ch == 4):
                    return self.showTable()
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.yearTable(year)
            elif(year == 2):
                if(ch == 1):
                    self.CSE_display(2)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return self.showTable()
                elif (ch == 2):
                    self.CSE_display(3)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return self.showTable()
                elif (ch == 3):
                    self.CSE_display(4)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return self.showTable()
                elif (ch == 4):
                    return self.showTable()
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.yearTable(temp)
            elif(year == 3):
                if(ch == 1):
                    self.CE_display(2)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return stud.displayBook()
                elif (ch == 2):
                    self.CE_display(3)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return stud.displayBook()
                elif (ch == 3):
                    self.CE_display(4)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return stud.displayBook()
                elif (ch == 4):
                    return stud.displayBook()
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.yearTable(year)
            elif(year == 4):
                if(ch == 1):
                    self.CSE_display(2)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return stud.displayBook()
                elif (ch == 2):
                    self.CSE_display(3)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return stud.displayBook()
                elif (ch == 3):
                    self.CSE_display(4)
                    input("Press Enter to continue...")
                    os.system("clear")
                    return stud.displayBook()
                elif (ch == 4):
                    return stud.displayBook()
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.yearTable(temp)
        except ValueError:
            print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
            os.system("clear")
            return self.yearTable(year) 
        
    def showTable(self):
        try:
            menu = ('''
                [bold green]+-----------+--------------+---------------------------------------+[/bold green ]
                [bold green]|[bold cyan]   Sr.no[/bold cyan]   | [bold cyan]Branch Code[/bold cyan]  |[/bold green][bold cyan]                  Trade                [/bold cyan][bold green]|[/bold green]
                [bold green]+-----------+--------------+---------------------------------------+[/bold green]
                [bold green]|[/bold green]     1.    [bold green]|[/bold green][bold cyan]    CE        [/bold cyan][bold green]|[/bold green][bold cyan] Computer Enginnering(CE)[/bold cyan]           [bold green]   |[/bold green]
                [bold green]|[/bold green]     2.    [bold green]|[/bold green][bold cyan]    CSE       [/bold cyan][bold green]|[/bold green][bold cyan] Computer Science Enginnering(CSE)[/bold cyan]  [bold green]   |[/bold green]
                [bold green]|[/bold green]     3.    [bold green]|[/bold green][bold cyan]     -        [/bold cyan][bold green]|[/bold green][bold cyan] Show Issued books[/bold cyan]                  [bold green]   |[/bold green]
                [bold green]|[/bold green]     4.    [bold green]|[/bold green][bold cyan]     -        [/bold cyan][bold green]|[/bold green][bold cyan] Back To Menu[/bold cyan]                       [bold green]   |[/bold green]
                [bold green]+-----------+--------------+---------------------------------------+[/bold green]''')
            
            print(menu)
            ch = int(input("\t\t ~ Enter: "))
            os.system("clear")
            if ch == 1:
                self.yearTable(1)
            elif ch == 2:
                self.yearTable(2)
            elif ch == 3:
                self.showissued()
                input("Press Enter to continue...")
                os.system("clear")
            elif ch == 4:
                athe = authenticate()
                athe.menu()
            else:
                os.system("clear")
                print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                return self.showTable()
        except ValueError:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
            return self.showTable()
        
    def issue(self,table):
        extractCode = []
        extractid = []
        mycrc.execute(f"SELECT Book_code FROM {table}")
        try:
            for x in mycrc:
                extractCode.append(x[0])
            db.commit()
            id = int(input("\n~ Enter the Student id: "))
            mycrc.execute(f"SELECT ID FROM student")
            for i in mycrc:
                extractid.append(i[0])
            db.commit()
            if id in extractid:    
                bcode = int(input("~ Enter Book code: "))
                if bcode in extractCode:
                    mycrc.execute(f"select status from {table} where Book_code = {bcode}")
                    for i in mycrc:
                        check = i[0]
                    db.commit()

                    if check == "avaliable":
                        status = True
                    else:
                        status = False
                else:
                    print("\n[bold red]SEARCH ERROR:[bold red] [bold green]Book is not present in the list...[bold green]")
            else:
                print("\n[bold red]SEARCH ERROR:[bold red] [bold green]ID that mentioned doesn't exist...[bold green]")
        except:
            print("\n[bold red]ERROR: Falied to fetch the book[/bold red] ")
        try:
            mycrc.execute(f"SELECT books from {table} WHERE Book_code = {bcode}")
            for data in mycrc:
                book = data[0]
            db.commit()
            mycrc.execute(f"select Student_name from student where iD = {id}")
            for i in mycrc:
                name = i[0]
            db.commit()
            if bcode in extractCode and status == True:
                mycrc.execute(f"UPDATE {table} SET status = 'issued' WHERE Book_code = {bcode}")
                db.commit()
                mycrc.execute("INSERT INTO issue_book VALUES(%s,%s,%s,%s)",(bcode,book,id,name))
                db.commit()
                print("[bold green]Processing...[/bold green]")
                sleep(2.0)
                print("\n[bold green]Success:[/bold green] [bold cyan]Book is issued successfully [/bold cyan]")
            elif status == False:
                print("[bold red]ERROR: Book is already issued[/bold red]")
        except:
            print("[bold red]ERROR: The value you entered is wrong!![/bold red]")

    def removeBook(self,table):
        extractBook = []
        mycrc.execute(f"SELECT Book_code from {table}")
        try:
            for i in mycrc:
                extractBook.append(i[0])
            db.commit()
            bcode = int(input("~ Enter the valid Book_code: "))
            if bcode in extractBook:
                mycrc.execute(f"SELECT status FROM {table} WHERE Book_code = {bcode}")
                for i in mycrc:
                    check = i[0]
                db.commit()
                print("\n[bold green]Processing...[/bold green]")
                sleep(2.0)
                if check == "avaliable":
                    print("[bold green]Sucess: [/bold green][bold cyan]Book is avaliabe....[/bold cyan]")
                    status = True
                else:
                    print("[bold red]Search Error: [/bold red][bold cyan]Sorry, Book is issued....[/bold cyan]")
                    status = False
            else:
                print("[bold red]Search Error: [/bold red]The Book code you mentioned doesn't exist")
        except:
            print("[bold red]System Error: [/bold red] Failed to fetch the books...")
        try:
            if bcode in extractBook and status == True:
                print("Are you sure to [bold red]remove[/bold red] the mentioned book ??[bold green]Yes(Y or y) No(N or n))[/bold green]")
                choice = input("~ :")
                if choice == "Y" or choice == "y":
                    print("\n[bold green]Please Wait...[/bold green]")
                    sleep(2.0)
                    mycrc.execute(f"DELETE FROM {table} WHERE Book_code = {bcode}")
                    db.commit()
                    print("[bold green]Success: [bold green]Book is successfully removed from the list...")
                elif choice == "N" or choice == "n":
                    return self.removeBook()
                else:
                    print("[bold red]Warning!: Invalid Input [bold red]")
        except:
            print(" ")
        
    def Student(self):
            user = student()
            try:
                menu = (f'''\t\t\t\t\n          Date: {time}
                    [bold cyan][ Students Account ][/bold cyan]
                        1. Add a User.
                        2. Show list of User's.
                        3. Update user's info.
                        4. Delete the user.
                        5. Back to Menu.''')
                print(menu)
                ch = int(input("\t\t~ Enter: "))
                os.system("clear")
                if ch == 1:
                    print("\n[bold yellow underline][ Note: Please enter the info correctly.][/bold yellow underline] \n\n[bold green][+] Adding user...[/bold green]")
                    id = int(input("[+] Create a Id     ~: "))
                    name = input("[+] Enter Full name ~: ")
                    trade = input("[+] Trade           ~: ")
                    contact = int(input("[+] contact number  ~: "))
                    conlen = str(contact)
                    if len(conlen) == 10:
                        Email = input("[+] Email           ~:")
                        user.addStudent(id,name,trade,contact,Email)
                    else:
                        print("[bold red]ERROR: [/bold red]Invalid contact number...")
                        input("Press Enter to continue...")
                        os.system("clear")
                        return self.Student()
                            
                elif ch == 2:
                    user.showStudent()
                    input("Press Enter to continue...")
                    os.system("clear")
                
                elif ch == 3:
                    id = int(input("~ Enter the Students id: "))
                    user.updateStudent(id)
                    input("Press Enter to continue...")
                    os.system("clear")
                
                elif ch == 4:
                    id = int(input("~ Enter the Students id: "))
                    user.removeStudent(id)
                    input("Press Enter to continue...")
                    os.system("clear")

                elif ch == 5:
                    ath = authenticate()
                    ath.menu()
                    input("Press Enter to continue...")
                    os.system("clear")
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.Student()
            except ValueError:
                os.system("clear")
                print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                return self.Student()

    def returnBook(self,id,bcode,table):
        extractid = []
        extractCode = []
        try:
            mycrc.execute("select ID from student")
            for i in mycrc:
                extractid.append(i[0])
            db.commit()
            mycrc.execute(f"select Book_code from {table}")
            for i in mycrc:
                extractCode.append(i[0])
            db.commit()
            if id in extractid:
                if bcode in extractCode:
                    mycrc.execute(f"select Status from {table} where Book_code = {bcode}")
                    for i in mycrc:
                        check = i[0]
                        # print(check)
                    db.commit()
                    if check == "issued":
                        status = True
                    else:
                        status = False
                    exBid = []
                    mycrc.execute(f"select id from issue_book where Book_code = {bcode}")
                    for i in mycrc:
                        exBid.append(i[0])
                    db.commit()
                    if id in exBid:
                        if status == True:
                            mycrc.execute(f"update {table} set Status = 'avaliable' where Book_code = {bcode}")
                            db.commit()
                            mycrc.execute(f"delete from issue_book where id = {id}")
                            db.commit()
                            print("[bold green]Processing....[/bold green]")
                            sleep(2.0)
                            print("[bold green]Success: [bold cyan]Details Updated Successfully....[/bold cyan][/bold green]")
                        elif status == False:
                            print("[bold red]ERROR: [bold cyan]The book you mentioned is already avaliable....[/bold cyan][/bold red]")
                    else:
                        print("[bold yellow]Note: [bold cyan underline]The student you mention, Doesn't borrowed the book....[/bold cyan underline][/bold yellow]")
                else:
                    print("[bold red]Search Error: [/bold red]The Book code you mentioned doesn't exist")
            else:
                print("[bold red]Search Error: [/bold red]The ID you mentioned doesn't exist")
        except ValueError:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
            return self.returnBook()
    
    def addAdmin(self,user,passwd):
        mycrc.execute("insert into admin values(%s,%s)",(user,passwd))
        db.commit()
        print("[bold green]Processing[/bold green]")
        sleep(2.0)
        print("\n[bold green]Success: [bold cyan]New Admin is added successfully....[/bold cyan][/bold green]")
        input("Press Enter to continue...")
    
    def deleteAdmin(self,user,paswd):
        listuser = []
        mycrc.execute("select username from admin")
        for i in mycrc:
            listuser.append(i[0])
        db.commit()
        listpasswd = []
        mycrc.execute("select passwd from admin")
        for i in mycrc:
            listpasswd.append(i[0])
        db.commit()
        listadmin = {listuser[i]:listpasswd[i] for i in range(len(listuser))}
        if user in listadmin.keys():
            password = listadmin[user]
            if paswd == password:
                mycrc.execute(f"delete from admin where username = '{user}'")
                db.commit()
                print("\n[bold green]Success: [bold cyan]Admin Deleted Successfully.[/bold cyan][/bold green]")
            else:
                print("\n[bold red]ERROR: Wrong Password. . .[/bold red]")
        else:
            print("\n[bold red]ERROR: Invalid Admin.[bold red]")

    def menuAdmin(self):
        menu = (f'''\t\t\t\t\n          Date: {time}
                    [bold cyan][ Menu ][/bold cyan]
                    1. Add new Admin.
                    2. Delete a Admin.
                    3. Back.''')
        print(menu)
        ch = int(input("\t\t~ Enter: "))
        try:
            if ch == 1:
                print("\n[bold cyan][ Adding new admin ][/bold cyan]")
                name = input("\n~ Enter new Username: ")
                passwd = input("~ Enter new Password: ")
                self.addAdmin(name,passwd)
                os.system("clear")
            
            elif ch == 2:
                print("\n[bold cyan][ Deleting admin ][/bold cyan]")
                name = input("\n~ Enter  Username: ")
                passwd = input("~ Enter  Password: ")
                self.deleteAdmin(name,passwd)
                input("Press Enter to continue...")
                os.system("clear")
            
            elif ch == 3:
                athu = authenticate()
                athu.menu()
            
            else:
                os.system("clear")
                print("[bold red]ERROR: Invalid Choice [/bold red]")
                return self.menuAdmin()
        except ValueError:
            os.system("clear")
            print("[bold red]ERROR: Invalid Choice [/bold red]")
            return self.menuAdmin()

class student:
    def addStudent(self,id,name,trade,contact,email):
        try:
            print("[bold green][+] Done!![/bold green]\n")
            print("[bold green]Processing...[/bold green]")
            sleep(2.0)
            print("\n[bold yellow]Note: [/bold yellow][bold cyan]Create the Username and a strong password....[/bold cyan]")
            user = input("~ Username: ")
            passwd = input("~ Password: ")
            mycrc.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(id,name,trade,contact,email,user,passwd))
            db.commit()
            print("[bold green]Success: [/bold green]Account Successfully Created...")
            input("Press Enter to continue...")
            os.system("clear")
        except ValueError:
            print("[bold red]ERROR: [/bold red]Invalid input..")
            input("Press Enter to continue...")
            os.system("clear")
    
    def showStudent(self):
        dbtable = PrettyTable()
        print("[bold cyan]-----------------------------------------User list-----------------------------------------------[bold cyan]")
        dbtable.field_names = ["ID","Student_name","Trade","Contact","Email","Username","Password"]
        mycrc.execute("select * from student")
        for data in mycrc:
            dbtable.add_row(data)
        print(dbtable)
        db.commit()

    def updateStudent(self,id):
        extractid = []
        mycrc.execute("select ID from student")
        try:
            for i in mycrc:
                extractid.append(i[0])
            db.commit()

            if id in extractid:
                menu = (f'''\t\t\t\t\n          Date: {time}
                    [bold cyan][ Choice, which info you want to change ][/bold cyan]
                    1. Trade.
                    2. Contact.
                    3. Email.''')
                print(menu)
                try:
                    ch = int(input("\t\t~ Enter: "))
                    if ch == 1:
                        trade = input("~ Enter the valid Trade: ")
                        mycrc.execute(f"update student set Trade = '{trade}' where ID = {id}")
                        db.commit()
                        print("[bold cyan]Details are successfully Updated..[/bold cyan]")
                    
                    elif ch == 2:
                        contact = int(input("~ Enter the valid Contact number: "))
                        con = str(contact)
                        if len(con) == 10:
                            mycrc.execute(f"update student set Contact = '{contact}' where ID = {id}")
                            db.commit()
                            print("[bold cyan]Details are successfully Updated..[/bold cyan]")
                        else:
                            print("[bold red]ERROR: [/bold red]PLease kindly enter valid contact number")
                                                
                    elif ch == 3:
                        Email = input("~ Enter the valid Email: ")
                        mycrc.execute(f"update student set Email = '{Email}' where ID = {id}")
                        db.commit()
                        print("[bold cyan]Details are successfully Updated..[/bold cyan]")
                    else:
                        print("[bold red]ERROR: [/bold red]Invalid input...")
                except ValueError:
                    print("[bold red]ERROR: [/bold red]Invalid input...")
            else:
                print("[bold red]Result UnFound:[/bold red]The id you mentioned doesn't exist....")
        except ValueError:
            print("[bold red]ERROR: The value you entered is wrong!![/bold red]")

    def removeStudent(self,id):
        issueid =[]
        mycrc.execute("select id from issue_book")
        for i in mycrc:
            issueid.append(i[0])
        db.commit()
        print("[bold green]Please Wait...[/bold green]")
        sleep(1.0)
        if id in issueid:
            print("[bold yellow]Note: [bold cyan]The id has Borrowed books, Account can only be deleted after returning the book.[/bold cyan][/bold yellow]")
        else:
            try:
                extractid = []
                mycrc.execute("select ID from student")
                for i in mycrc:
                    extractid.append(i[0])
                db.commit()
                if id in extractid:
                    print("[bold yellow]Warning: [/bold yellow]Are you sure to remove the account??[bold green]Yes(Y or y),NO(N or n)[/bold green]")
                    choice1 = input("~ :")
                    if choice1 == "Y" or choice1 == "y":
                        mycrc.execute(f"delete from student where ID = {id}")
                        db.commit()
                        print("[bold green]Processing[/bold green]")
                        sleep(2.0)
                        print(f"All the details of id : {id}, is removed [bold green]successfully..[/bold green]")
                    elif choice1 == "N" or choice1 == "n":
                        extractid.clear()
                        self.removeStudent()
                    else:
                        print("[bold red]Warning!: Invalid Input [bold red]")
                else:
                    print("[bold red]ERROR: [bold cyan]Id Doesn't Exist[/bold cyan][/bold red]")
            except:
                print(" ")
            

    def displayBook(sel):
        a = administrator()
        menu = ('''
                    [bold green]+-----------+--------------+---------------------------------------+[/bold green ]
                    [bold green]|[bold cyan]   Sr.no[/bold cyan]   | [bold cyan]Branch Code[/bold cyan]  |[/bold green][bold cyan]                  Trade                [/bold cyan][bold green]|[/bold green]
                    [bold green]+-----------+--------------+---------------------------------------+[/bold green]
                    [bold green]|[/bold green]     1.    [bold green]|[/bold green][bold cyan]    CE        [/bold cyan][bold green]|[/bold green][bold cyan] Computer Enginnering(CE)[/bold cyan]           [bold green]   |[/bold green]
                    [bold green]|[/bold green]     2.    [bold green]|[/bold green][bold cyan]    CSE       [/bold cyan][bold green]|[/bold green][bold cyan] Computer Science Enginnering(CSE)[/bold cyan]  [bold green]   |[/bold green]
                    [bold green]|[/bold green]     3.    [bold green]|[/bold green][bold cyan]     -        [/bold cyan][bold green]|[/bold green][bold cyan] Back To Menu[/bold cyan]                       [bold green]   |[/bold green]
                    [bold green]+-----------+--------------+---------------------------------------+[/bold green]''')
        print(menu)
        ch = int(input("\t\t  ~ Enter: "))
        os.system("clear")
        try:
            if ch == 1:
                a.yearTable(3)
                input("Press Enter to continue...")
                os.system("clear")
            elif ch == 2:
                a.yearTable(4)
                input("Press Enter to continue...")
                os.system("clear")
            elif ch == 3:
                athu = authenticate()
                athu.menustudent()      
            else:
                os.system("clear")
                print("[bold red]ERROR: Invalid Input[/bold red]")
                return sel.displayBook()
        except ValueError:
            os.system("clear")
            print("[bold red]ERROR: Invalid Input[/bold red]")
            return sel.displayBook()
    
    def profile(self,id):
        idlist = []
        mycrc.execute(f"select ID from student")
        for i in mycrc:
            idlist.append(i[0])
        db.commit()
        if id in idlist:
            mycrc.execute(f"select ID from student where ID = {id}")
            for i in mycrc:
                studid = i[0]
            db.commit()
            mycrc.execute(f"select Student_name from student where ID = {id}")
            for i in mycrc:
                name = i[0]
            db.commit()
            mycrc.execute(f"select Trade from student where ID = {id}")
            for i in mycrc:
                trade = i[0]
            db.commit()
            mycrc.execute(f"select Contact from student where ID = {id}")
            for i in mycrc:
                contact = i[0]
            db.commit()
            prof = f'''[bold green]+-------------------------------------------------+[/bold green]
[bold green]|[bold yellow]                  My Profile                     [/bold yellow]|[/bold green]
[bold green]+----------+--------------------------------------+[/bold green]
[bold green]|[bold yellow]ID[/bold yellow]        |[/bold green][bold cyan]{studid}[/bold cyan]
[bold green]+----------+--------------------------------------+[/bold green]                        
[bold green]|[bold yellow]Name[/bold yellow]      |[/bold green][bold cyan]{name}[/bold cyan]
[bold green]+----------+--------------------------------------+[/bold green]
[bold green]|[bold yellow]Trade[/bold yellow]     |[/bold green][bold cyan]{trade}[/bold cyan]                          
[bold green]+----------+--------------------------------------+[/bold green]
[bold green]|[bold yellow]Conatact[/bold yellow]  |[/bold green][bold cyan]{contact}[/bold cyan]
[bold green]+----------+--------------------------------------+[/bold green]'''
            print(prof)
        input("Press Enter to continue...")
        os.system("clear")
        athu = authenticate()
        return athu.menustudent()

class authenticate:
    count = 3
    def menu(self):
        menu2 = ('''
                    [bold green]+-----------+--------------+---------------------------------------+[/bold green ]
                    [bold green]|[bold cyan]   Sr.no[/bold cyan]   | [bold cyan]Branch Code[/bold cyan]  |[/bold green][bold cyan]                  Trade                [/bold cyan][bold green]|[/bold green]
                    [bold green]+-----------+--------------+---------------------------------------+[/bold green]
                    [bold green]|[/bold green]     1.    [bold green]|[/bold green][bold cyan]    CE        [/bold cyan][bold green]|[/bold green][bold cyan] Computer Enginnering(CE)[/bold cyan]           [bold green]   |[/bold green]
                    [bold green]|[/bold green]     2.    [bold green]|[/bold green][bold cyan]    CSE       [/bold cyan][bold green]|[/bold green][bold cyan] Computer Science Enginnering(CSE)[/bold cyan]  [bold green]   |[/bold green]
                    [bold green]|[/bold green]     3.    [bold green]|[/bold green][bold cyan]     -        [/bold cyan][bold green]|[/bold green][bold cyan] Back To Menu[/bold cyan]                       [bold green]   |[/bold green]
                    [bold green]+-----------+--------------+---------------------------------------+[/bold green]''')
        try:
            admin = administrator()
            os.system("clear")
            menu1 = (f'''\t\t\t\t\n          Date: {time}
                    [bold cyan][ Menu ][/bold cyan]
                    1. Add Books to the library List.
                    2. Display The Books listed in library.
                    3. Remove a book from library. 
                    4. Issue book to student.
                    5. Edit students account. 
                    6. Return the book.
                    7. Edit Admin.
                    8. Log out.''')
            print(menu1)
            ch = int(input("\t\t~ Enter Choice: "))
            os.system("clear")
            choice = True
            while choice:
                if ch == 1:
                    try:
                        print(menu2)
                        ch2 = int(input("\t\t    ~ Enter: "))
                        os.system("clear")
                        if ch2 == 1:
                            print("\n[bold yellow underline][ Note: Please enter the info correctly.][/bold yellow underline] \n\n[bold green][+] Registering Book...[/bold green]")
                            book_name = input("[+] Book name               ~: ")
                            author = input("[+] Author name             ~: ") 
                            price = int(input("[+] Actual price            ~: "))
                            publisher = input("[+] Publisher               ~: ")
                            status = input("[+] Status(avaliable/issued)~: ")
                            print("[bold yellow ][+] Please mention for which [bold cyan ]Class Year[/bold cyan] this book is for....[bold yellow ]")
                            year = int(input("[+] Year (2,3,4)~: "))
                            print("[bold green][+] Done!![/bold green]")
                            admin.CE_addBooks(book_name,author,publisher,price,status,year)
                        elif ch2 == 2:
                            print("\n[bold yellow][ Note: Please enter the info correctly.][/bold yellow] \n\n[bold green][+] Registering Book...[/bold green]")
                            book_name = input("[+] Book name               ~: ")
                            author = input("[+] Author name             ~: ") 
                            price = int(input("[+] Actual price            ~: "))
                            publisher = input("[+] Publisher               ~: ")
                            status = input("[+] Status(avaliable/issued)~: ")
                            print("[bold yellow ][+] Please mention for which [bold cyan ]Class Year[/bold cyan] this book is for....[bold yellow ]")
                            year = int(input("[+] Year (2,3,4)~: "))
                            print("[bold green][+] Done!![/bold green]")
                            admin.CSE_addBooks(book_name,author,publisher,price,status,year)
                        elif ch2 == 3:
                            self.menu()
                        else:
                            os.system("clear")
                            print("[bold red]ERROR: Invalid choice[/bold red]")
                    except ValueError:
                        os.system("clear")
                        print("[bold red]ERROR: Invalid choice[/bold red]")
                elif ch == 2:
                    admin.showTable()
                elif ch == 3:
                    try:
                        print(menu2)
                        ch3 = int(input("~ Enter: "))
                        if ch3 == 1:
                            table = "ce_books"
                            admin.removeBook(table)
                            input("Press Enter to continue...")
                            os.system("clear")
                        elif ch3 == 2:
                            table = "cse_books"
                            admin.removeBook(table)
                            input("Press Enter to continue...")
                            os.system("clear")
                        elif ch3 == 3:
                            self.menu()
                        else:
                            os.system("clear")
                            print("[bold red]ERROR: Invalid choice[/bold red]")
                    except ValueError:
                        os.system("clear")
                        print("[bold red]ERROR: Invalid choice[/bold red]")
                elif ch == 4:
                    try:
                        print(menu2)
                        ch4 = int(input("~ Enter: "))
                        if ch4 == 1:
                            table = "ce_books"
                            admin.issue(table)
                            input("Press Enter to continue...")
                            os.system("clear")
                        elif ch4 == 2:
                            table = "cse_books"
                            admin.issue(table)
                            input("Press Enter to continue...")
                            os.system("clear")
                        elif ch4 == 3:
                            self.menu()
                        else:
                            os.system("clear")
                            print("[bold red]ERROR: Invalid choice[/bold red]")
                    except ValueError:
                        os.system("clear")
                        print("[bold red]ERROR: Invalid choice[/bold red]")
                elif ch == 5:
                    admin.Student()
                elif ch == 6:
                    try:
                        print(menu2)
                        ch5 = int(input("~ Enter: "))
                        if ch5 == 1:
                            id = int(input("~ Enter the Student ID: "))
                            bcod = int(input("~ Enter the Book Code: "))
                            table = "ce_books"
                            admin.returnBook(id,bcod,table)
                            input("Press Enter to continue...")
                            os.system("clear")
                        elif ch5 == 2:
                            id = int(input("~ Enter the Student ID: "))
                            bcod = int(input("~ Enter the Book Code: "))
                            table = "cse_books"
                            admin.returnBook(id,bcod,table)
                            input("Press Enter to continue...")
                            os.system("clear")
                        elif ch5 == 3:
                            self.menu()
                        else:
                            os.system("clear")
                            print("[bold red]ERROR: Invalid choice[/bold red]")
                    except ValueError:
                        os.system("clear")
                        print("[bold red]ERROR: Invalid choice[/bold red]")
                elif ch == 7:
                    admin.menuAdmin()
                elif ch == 8:
                    self.verify()
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.menu()
        except ValueError:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
            return self.menu()
    
    def menustudent(self):
        admin = student()
        os.system("clear")
        choice = True
        menu = (f'''\t\t\t\t\n          Date: {time}
                    [bold cyan][ Menu ][/bold cyan]
                    1. Display The Avaliable Books.
                    2. See your profile.
                    3. Log out''')
        print(menu)
        ch = int(input("\t\t~ Enter: "))
        os.system("clear")
        while choice:
            try:
                if ch == 1:
                    admin.displayBook()
                elif ch == 2:
                    for i in cuuruser:
                        data = i
                    mycrc.execute(f"select ID from student where username = '{data}'")
                    for i in mycrc:
                        id = i[0]
                    db.commit()
                    admin.profile(id)
                elif ch == 3:
                    self.verifyStudent()
                else:
                    os.system("clear")
                    print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                    return self.menustudent()
            except ValueError:
                os.system("clear")
                print("\n\t[bold red]ERROR: Invalid Choice[/bold red]")
                return self.menustudent()

    def verify(self):
        log = login()
        print("\n\n\n")
        print("\t\t[bold green]+-------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold red]                     ALERT                       [/bold red][bold green]|[/bold green]")
        print("\t\t[bold green]+-------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold cyan]                [Logging out]                    [/bold cyan][bold green]|[/bold green]")
        print("\t\t[bold green]+-------------------------------------------------+[/bold green]")
        print("\t\tYou are about [bold cyan]Log out[/bold cyan], are you sure?? [bold green]Yes(Y or y), No(N or n)[/bold green]")
        ch3 = input("                ~ : ")
        if ch3 == "Y" or ch3 == "y":
            os.system("clear")
            log.excute()
        elif ch3 == "N" or ch3 == "n":
            return self.menu()
        else:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Choice[/bold red]") 
            return self.verify()
   
    def verifyStudent(self):
        log = login()
        print("\n\n\n")
        print("\t\t[bold green]+-------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold red]                     ALERT                       [/bold red][bold green]|[/bold green]")
        print("\t\t[bold green]+-------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold cyan]                [Logging out]                    [/bold cyan][bold green]|[/bold green]")
        print("\t\t[bold green]+-------------------------------------------------+[/bold green]")
        print("\t\tYou are about [bold cyan]Log out[/bold cyan], are you sure?? [bold green]Yes(Y or y), No(N or n)[/bold green]")
        ch3 = input("                ~ : ")
        if ch3 == "Y" or ch3 == "y":
            os.system("clear")
            log.excute()
            cuuruser.clear()
        elif ch3 == "N" or ch3 == "n":
            return self.menustudent()
        else:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Choice[/bold red]") 
            return self.verifyStudent()
   
    def administrator(self):
        self.count-=1
        back = login()
        if(self.count == 0):
            os.system("clear")
            return back.excute()
        print("\n\n\n")
        print(f"\t\t                                                  You have {self.count} attempts left...")
        print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold cyan]                            Adiminstrator Login                            [/bold cyan][bold green]|[/bold green]")
        print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold cyan]            [ Please enter the Valid Username and password ]               [/bold cyan][bold green]|[/bold green]")
        print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
        user =  input("\t\t~ Username: ")
        passw = getpass("\t\t~ Password: ")
        print("\n")
        processing()
        listuser = []
        mycrc.execute("select username from admin")
        for i in mycrc:
            listuser.append(i[0])
        db.commit()
        listpasswd = []
        mycrc.execute("select passwd from admin")
        for i in mycrc:
            listpasswd.append(i[0])
        db.commit()
        listadmin = {listuser[i]:listpasswd[i] for i in range(len(listuser))}
        if user in listadmin.keys():
            password = listadmin[user]
            if passw == password:
                print("[bold green]Success: [bold cyan]Access Granted[/bold cyan][/bold green]")
                self.menu()
            else:
                os.system("clear")
                print("\n\t[bold red]ERROR: Wrong Password. . .[/bold red]")
                return self.administrator()
        else:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Admin.[bold red]")
            return self.administrator()
            
    def student(self):
        self.count-=1
        back = login()
        if(self.count == 0):
            os.system("clear")
            return back.excute()
        print("\n\n\n")
        print(f"\t\t                                                  You have {self.count} attempts left...")
        print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold cyan]                            Student Login                                  [/bold cyan][bold green]|[/bold green]")
        print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
        print("\t\t[bold green]|[/bold green][bold cyan]            [ Please enter the Valid Username and password ]               [/bold cyan][bold green]|[/bold green]")
        print("\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
        user =  input("\t\t~ Username: ")
        passw = getpass("\t\t~ Password: ")
        print("\n")
        processing()
        listuser = []
        mycrc.execute("select username from student")
        for i in mycrc:
            listuser.append(i[0])
        db.commit()
        listpasswd = []
        mycrc.execute("select passwd from student")
        for i in mycrc:
            listpasswd.append(i[0])
        db.commit()
        dictuser = {listuser[i]:listpasswd[i] for i in range(len(listuser))}
        if user in dictuser.keys():
            cuuruser.append(user)
            password = dictuser[user]
            if passw == password:
                print("\n\t[bold green]Success: [/bold green][bold cyan]Wellcome Back. . .[/bold cyan]")
                self.menustudent()
            else:
                os.system("clear")
                print("\n\t[bold red]ERROR: Wrong Password. . .[/bold red]")
                return self.student()
        else:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Username or Password...[bold red]")
            return self.student()

class login:
    def excute(self):
        os.system("clear")
        git_logo = '''[bold italic]
        \t\t\t████████╗████████╗████████╗ 
        \t\t\t██╔═════╝╚══██╔══╝╚══██╔══╝
        \t\t\t██║  ████╗  ██║      ██║
        \t\t\t██║   ██╔╝  ██║      ██║
        \t\t\t ██████╔╝████████╗   ██║
        \t\t\t ╚═════╝ ╚═══════╝   ╚═╝[/bold italic]'''
        lib_logo = '''[bold italic]
        \t\t\t██╗    ████████╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
        \t\t\t██║    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        \t\t\t██║       ██║   ██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
        \t\t\t██║       ██║   ██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝
        \t\t\t██████╗████████╗██████╔╝██║  ██║██║  ██║██║  ██║   ██║
        \t\t\t╚═════╝╚═══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝  [/bold italic]'''
        console.print(git_logo,end="",style="rgb(0,255,255)")
        console.print(lib_logo,style="rgb(255,255,26)")
        try:
            print("\n")
            print("\t\t\t\t [bold cyan italic]Welcome to our institute![/bold cyan italic] [bold magenta]We're glad to have you here.[/bold magenta] 📚📖🏛️")
            print("\t\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            print("\t\t\t[bold green]|                               [ LOGIN ]                                   |[/bold green]")
            print("\t\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            print("\t\t\t[bold green]|                                                                           |[/bold green]")
            print("\t\t\t[bold green]|[/bold green][bold cyan]                        1. Adiminstrator Login                            [/bold cyan] [bold green]|[/bold green]")
            print("\t\t\t[bold green]|[/bold green][bold cyan]                        2. Student Login                                  [/bold cyan] [bold green]|[/bold green]")
            print("\t\t\t[bold green]|[/bold green][bold cyan]                        3. Quit                                           [/bold cyan] [bold green]|[/bold green]")
            print("\t\t\t[bold green]+---------------------------------------------------------------------------+[/bold green]")
            ch = int(input("\t\t\t~ Enter: "))
            os.system("clear")
            lib = authenticate()
            if ch == 1:
                lib.administrator()
            elif ch == 2:
                lib.student()
            elif ch == 3:
                exit()
            else:
                os.system("clear")
                print("\n\t[bold red]ERROR: Invalid Input!![/bold red]")
                return self.excute()
        except ValueError:
            os.system("clear")
            print("\n\t[bold red]ERROR: Invalid Input!![/bold red]")
            return self.excute()

log = login()
log.excute()