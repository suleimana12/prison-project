import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
db=sqlite3.connect(":memory:")
sd=db.cursor()
sd.execute("create table Person (Id integer primary key,firstName text,father text ,lastName text,gender text,birthYear text,address text)")
sd=db.cursor()
sd.execute("create table Visitings (Id integer primary key,dateVisited integer,personld integer ,visitorName text,mountinminutes text,foreign key(personld) references Person(Id))")
sd.execute("create table Offense (Id integer primary key,name text,foreign key(Id) references Person(Id))")
sd.execute("create table Convicts (Id integer,fromDate text,toDate text ,personid integer,offenseid integer)")
sd.execute("create table Dungeon (id integer primary key,name text,size integer)")
sd.execute("create table DungeonMoves (Id integer primary key,dungeonid integer,personid integer,fromDate integer,foreign key(dungeonid) references Dungeon(Id),foreign key(personid) references Person(Id))" )

sd.execute('insert into person values (1,"mustafa","ali","rhmun","menton","1999","idlib")')
sd.execute('insert into person values (2,"abraham","abdo","ziadi","menton","2002","idlib")')
sd.execute('insert into person values (3,"ishmael","adam","hgteb","menton","2007","idlib")')
sd.execute('insert into person values (4,"yoseph","abraham","akte","menton","2005","idlib")')
sd.execute('insert into person values (5,"ayob","moses","hamed","menton","2009","idlib")')

sd.execute('insert into Visitings values(1,2010,1,"ahmad","one hour")')
sd.execute('insert into Visitings values(2,2012,2,"mustafa","one hour")')
sd.execute('insert into Visitings values(3,2015,5,"yamen","one hour")')
sd.execute('insert into Visitings values(6,2018,6,"asme","one hour")')
sd.execute('insert into Visitings values(5,2017,3,"yasir","one hour")')

sd.execute('insert into Offense values(1,"thief")')
sd.execute('insert into Offense values(2,"political crimes")')
sd.execute('insert into Offense values(3,"discredit")')
sd.execute('insert into Offense values(4,"scam")')
sd.execute('insert into Offense values(5,"thief")')

sd.execute('insert into Convicts values(1,"2010","01/01/2012",1,1)')
sd.execute('insert into Convicts values(2,"2012","01/01/2013",2,2)')
sd.execute('insert into Convicts values(3,"2013","01/01/2014",3,3)')
sd.execute('insert into Convicts values(4,"2014","01/01/2015",3,1)')
sd.execute('insert into Convicts values(5,"2015","01/01/2016",4,1)')

sd.execute('insert into Dungeon values(1,"dungeon for killers", 1)')
sd.execute('insert into Dungeon values(2,"criminals dungeon", 2)')
sd.execute('insert into Dungeon values(3,"single for killers",2)')
sd.execute('insert into Dungeon values(4,"single for criminals", 2)')


sd.execute('insert into DungeonMoves values(1,1,1,2010)')
sd.execute('insert into DungeonMoves values(2,2,1,2012)')
sd.execute('insert into DungeonMoves values(3,1,3,2009)')
sd.execute('insert into DungeonMoves values(4,3,3,2010)')
sd.execute('insert into DungeonMoves values(5,4,3,2012)')




class Main(Tk):
    def __init__(self):
        super().__init__()

        #الحجم
        self.geometry('400x400')
        #العنوان
        self.title('بياتات السجن')
        person_btn=Button(self,text='person',command=lambda:person(),width=20,fg='red',bg='black',cursor='')#,font=''
        person_btn.grid(row=0,column=8)
        visitings_but=Button(self,text='Visitings',command=lambda:visitings(),width=20,fg='red',bg='black')
        visitings_but.grid(row=1,column=8,pady=10)
        offenseld_but=Button(self,text='Offense',command=lambda:offenseq(),width=20,fg='red',bg='black')
        offenseld_but.grid(row=2,column=8)
        convicts_but=Button(self,text='Convicts',command=lambda:convicts(),width=20,fg='red',bg='black')
        convicts_but.grid(row=3,column=8,pady=10)
        
        dungeon_b=Button(self,text='Dungeon',command=lambda:dungeon(),width=20,fg='red',bg='black').grid(row=4,column=8,pady=10)
        dungeonMoves_b=Button(self,text='DungeonMoves',command=lambda:ungeonMoves(),width=20,fg='red',bg='black').grid(row=5,column=8,pady=10)
        def person():
            Person().mainloop()
        def visitings():
            Visitings().mainloop()
            
        def offenseq():
            Offense().mainloop()
        
        def convicts():
            
            Convicts().mainloop()
        def dungeon():
            Dungeon().mainloop()
        def ungeonMoves():
            DungeonMoves().mainloop()
            
class Person(Tk):
    def __init__(self):
        super().__init__()
        # الحجم
        self.geometry('600x600')
        # العنوان
        self.title('المساجين')
        def insert():
            self.id=per_id.get()
            self.name=name.get()
            self.father=father.get()
            self.lname=lname.get()
            self.birth=birth.get()
            self.gender=gender.get()
            self.address=address.get()
            sd.execute('insert into person values (?,?,?,?,?,?,?)',(self.id,self.name,self.father,self.lname,self.gender,self.birth,self.address))
        def select():
          sd.execute('select * from person')
          m=sd.fetchall()
          inf=''
          for i in m:
              inf+=f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}\n'
          messagebox.showinfo('',inf)
        Label(self,text='إضافة بيانات سجناء',fg='white',bg='black').grid()
        Label(self,text='Id',fg='white',bg='black').grid()
        per_id=Entry(self,fg='red',bg='white')
        per_id.grid()
        Label(self,text='name',fg='white',bg='black').grid()
        name=Entry(self,fg='red',bg='white')
        name.grid()
        Label(self,text='father',fg='white',bg='black').grid()
        father=Entry(self,fg='red',bg='white')
        father.grid()
        Label(self,text='last name',fg='white',bg='black').grid()
        lname=Entry(self,fg='red',bg='white')
        lname.grid()
        Label(self,text='gender',fg='white',bg='black').grid()
        gender=Entry(self,fg='red',bg='white')
        gender.grid()
        Label(self,text='birth',fg='white',bg='black').grid()
        birth=Entry(self,fg='red',bg='white')
        birth.grid()
        Label(self,text='address',fg='white',bg='black').grid()
        address=Entry(self,fg='red',bg='white')
        address.grid()
        Label(self,text='إضافة السحين الجديد',fg='white',bg='black').grid()
        sel_btn=Button(self,text='insert',command=insert,width=20,fg='white',bg='red')
        sel_btn.grid(pady=10)
        Label(self,text='الإستعلام عن السجناء',fg='white',bg='black').grid()
        sel_btn=Button(self,text='select',command=select,width=20,fg='white',bg='blue')
        sel_btn.grid(pady=10)
        

        def between():
            sd.execute('select * from Person where birthYear between ? and ?',(num1.get(),num2.get()))
            mw=sd.fetchall()
            sq=''
            for i in mw:
                sq+=f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}\n'
            messagebox.showinfo('ggggg',sq)
        
        Label(self,text='بيانات السجناء مابين زمنين',fg='white',bg='black').grid(row=0,column=3)
        Label(self,text='Enter num 1 ',fg='white',bg='black').grid(row=1,column=2,pady=10)
        num1=Entry(self,fg='red',bg='white')
        num1.grid(row=1,column=3)
        Label(self,text='Enter num 2 ',fg='white',bg='black').grid(row=2,column=2)
        num2=Entry(self,fg='red',bg='white')
        num2.grid(row=2,column=3)
        
        between_btn=Button(self,text='betwenn',command=between,fg='white',bg='red')
        between_btn.grid(row=3,column=3,pady=10)  
       
        def delete():
            sd.execute('delete from Person where Id= ? ',(delete1.get()))
        Label(self,text='Enter delete ',fg='white',bg='black').grid(row=4,column=3)
        delete1=Entry(self,fg='red',bg='white')
        delete1.grid(row=5,column=3,pady=10)
        delete1_but=Button(self,text='delete',command=delete,fg='white',bg='red').grid(row=6,column=3)
class Visitings(Tk):
    def __init__(self):
        super().__init__()
        # الحجم
        self.geometry('400x400')
        # العنوان
        self.title('الزيارات')
        def select():
            sd.execute("select * from Visitings")
            s=sd.fetchall()
            f=''
            for i in s:
                f+=f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n'
            messagebox.showinfo('',f)
        
        select_btn=Button(self,text='select',command=select,width=20,fg='white',bg='red')
        select_btn.grid()

        def between2():
            sd.execute('select Visitings.Id,Visitings."dateVisited",Visitings.visitorName,firstName,Visitings."mountinminutes" from Person INNER JOIN visitings ON person.Id=visitings."personld" where dateVisited between ? and ?',(add.get(),add2.get()))
            sg=sd.fetchall()
            fg=''
            for i in sg:
                fg+=f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n'
            messagebox.showinfo('مابين رقمين',fg)

        Label(self,text='birth 1 ',fg='white',bg='black').grid()
        add=Entry(self,fg='red',bg='white')
        add.grid()
        Label(self,text='birth 2 ',fg='white',bg='black').grid()
        add2=Entry(self,fg='red',bg='white')
        add2.grid()
        select_btn=Button(self,text='between',command=between2,width=20,fg='white',bg='red')
        select_btn.grid()
        
class Offense(Tk):
    def __init__(self):
        
        super().__init__()
        self.geometry('400x400')
        self.title('المحكوميات')

        def select():
            sd.execute("select * from Offense")
            d=sd.fetchall()
            df=''
            for i in d:
                df+=f'{i[0]},{i[1]}\n'
            messagebox.showinfo('',df)
        select_but=Button(self,text='select',command=select,width=20,fg='white',bg='red')
        select_but.grid()


        def off():
            # sd.execute('select firstName, Offense.name from Person INNER JOIN Offense ON person.Id=Offense.Id where name=?',(Name.get()))
            sd.execute('SELECT offense.id,offense.name,firstname, lastname from person,offense INNER JOIN convicts ON person.id= convicts.personid where offenseid=? and offense.id=convicts.offenseid',(ofid.get(),))
            h=sd.fetchall()
            sa=''
            for i in h:
                sa+=f'{i[0]},{i[1]},{i[2]},{i[3]}\n'
            messagebox.showinfo('',sa)
            
        Label(self,text='ID').grid()
        ofid=Entry(self,fg='red',bg='white')
        ofid.grid()
        off_but=Button(self,text='select',command=off,width=20,fg='white',bg='red')
        off_but.grid()

class Convicts(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('المحكوميات')
        def select():
            sd.execute("select * from Convicts " )
            d=sd.fetchall()
            fd=''
            for i in d:
                fd+=f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n'
            messagebox.showinfo('المحكوميات',fd)

        selectc_but=Button(self,text='Select',command=select,width=20,height=2,fg='white',bg='red')
        selectc_but.grid(row=0,column=0)
        
        def between():
            
            sd.execute('select * from Convicts where fromDate between ? and ?',(date.get(),date2.get()))
            f=sd.fetchall()
            g=''
            for i in f:
                g+=f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n'
            messagebox.showinfo('',g)
        Label(self,text='Enter date 1',fg='white',bg='black').grid(row=0,column=6)
        date=Entry(self,fg='red',bg='white')
        date.grid(row=1,column=6)
        Label(self,text='Enter date 2',fg='white',bg='black').grid(row=2,column=6)
        date2=Entry(self,fg='red',bg='white')
        date2.grid(row=3,column=6)
        between_fro=Button(self,text='between',command=between,width=10,fg='white',bg='red')
        between_fro.grid(row=4,column=6,pady=10)
       
class Dungeon(Tk):
    def __init__(self):
        super().__init__()    
        self.geometry('400x400')
        self.title('المحكوميات')
        def select():
            sd.execute("select * from Dungeon")
            s=sd.fetchall()
            d=''
            for i in s:
                d+=f'{i[0]},{i[1]},{i[2]}\n'
            messagebox.showinfo('',d)
        selectd=Button(self,text='Select',command=select,fg='white',bg='red').grid()
        
        
class DungeonMoves(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('400x400') 
        self.title('الزنزانات')
        def select():
            
            sd.execute("select * from DungeonMoves")
            n=sd.fetchall()
            f=''
            for i in n:
                f+=f'{i[0]},{i[1]},{i[2]},{i[3]}\n'
            messagebox.showinfo('',f)
        dun=Button(self,text='Select',command=select,fg='white',bg='red').grid(pady=10)
        def Dungeonblass():
            sd.execute('select dungeonmoves.id,dungeonmoves.fromdate,dungeonmoves.personid,dungeonmoves.dungeonid, firstname, lastname ,dungeon.name from person,dungeon INNER JOIN dungeonmoves ON person.id= dungeonmoves.personid where person.id=? and dungeon.id=dungeonmoves.dungeonid',(pid.get()))
            # sd.execute('SELECT Offense.Id,Offense.name,firstname, lastname from person,Offense INNER JOIN Convicts ON person.Id= Convicts.personid where Offense.Id=Convicts.OffenseId')
            h=sd.fetchall()
            d=''
            for i in h:
                d+=f'{i[0]},{i[1]},{i[2]},{i[4]},{i[5]},{i[6]}\n'
            messagebox.showinfo('',d)
            
        Label(self,text='Enter date 1',fg='white',bg='black').grid()

        pid=Entry(self,fg='red',bg='white')
        pid.grid()
                  
            
        dun=Button(self,text='Search',command=Dungeonblass,fg='white',bg='red').grid()

            
        
       
Main().mainloop()





















