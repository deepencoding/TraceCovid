import sqlite3
import pandas as pd
import os




FIELDS=['SNO','NAME_OF_HOSPITAL','ADDRESS_OF_HOSPITAL','CONTACT','TOTAL_BEDS','VACANT_BEDS','RECOVERY_RATE','TOTAL_DEATHS']

conn=sqlite3.connect('TraceCovid.db')

c=conn.cursor()

c.executescript('''Create table if not exists delhi (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (95),CONTACT  int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists mumbai (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (115),CONTACT int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists kolkata (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (115),CONTACT int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists chennai (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (115),CONTACT int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists CASES(SNO int,NAME_OF_CITY varchar(17),TOTAL_CASES INT(37),RECOVERED_CASES INT(40),DEATHS INT(35));

CREATE TABLE IF NOT EXISTS PRICES(SNO INT,ISOLATION_BEDS VARCHAR(45),ICU_BEDS_WITH_VENTILATOR VERCHAR(45),ICU_BEDS_WITHOUT_VENTILATOR VARCHAR(45));

create table if not exists INDIA(TOTAL_CASES varchar,RECOVERED varchar,DEATHS varchar);

create table if not exists user_data(SNO int, PASSWD varchar(30) default'000');
''')
conn.commit()

"""
c.executescript('insert into INDIA values("8.04M","7.32M","121K")')
conn.commit()



c.execute('insert into user_data values(1,"root");')
conn.commit()

c.executescript('''insert into delhi values(1,'LOK NAYAK HOSPITAL','JAWAHARLAL NEHRU MARG, NEW DELHI-110002',1123236000,2000,1276,73.37,295);

insert into delhi values(2,'RAJIV GANDHI SUPER SPECIALITY HOSPITA;','TAHIRPUR VILLAGE, DILSHAD GARDEN, NEW DELHI-110093',01122890604,1990,750,69.32,310);

insert into delhi values(3,'RAM MANOHAR LOHIA HOSPITAL','BABA KHARAK SINGH ROAD,CONNAUGHT PLACE, NEW DELHI-110001',01123365525,236,92,44.28,122);

insert into delhi values(4,'St. STEPHENS HOSPITAL','TIS HAZARI, NEW DELHI-110054',0112396021,250,192,68.89,198);
''')
conn.commit()




c.executescript('''insert into mumbai values(1,'BOMBAY HOSPITAL AND MEDICAL RESEARCH CENTRE','12 VITTHALDAS THACKERSEY MARG, NEW MARINE LINES, MUMBAI, MAHARASHTRA-400020',0222206767,90,11,78.43,34);

insert into mumbai values(2,'SAIFEE HOSPITAL','15/17 MAHARASHI KARVE ROAD,CHARNI ROAD EAST,GURGAON,MUMBAI,MAHARASHTRA-400004',0226757011,97,13,69.99,42);

insert into mumbai values(3,'BHATIA HOSPITAL','TARDEO ROAD,OLD CHIKALWADI,GRANT ROAD WEST,MUMBAI,MAHARASHTRA-400007',0226666000,80,10,88.4,23);

insert into mumbai values(4,'WOCKHARDT HOSPITAL','POLICE STATION,1877DOCTOR ANANDRAO NAIR MARG,MUMBAI CENTRAL,MUMBAI,MAHARASHTRA-400011',0829110100,128,30,88.8,19);
''')
conn.commit()

c.executescript('''insert into kolkata values(1,'M R BANGUR HOSPITAL','241-DESHPARAN SASMAL ROAD,NETAJI NAGAR RAJENDRA PRASAD COLONY,TOLLYGUNGE,KOLKATA,WEST BENGAL-700033',22202070,670,185,76.94,333);

insert into kolkata values(2,'DESUN HOSPITAL','DESUN MORE,720,EASTERN METROPOLITAN BYPASS,GOL PARK,SECTOR-I KASBA,KOLKATA,WEST BENGAL-700107',90517151,113,60,66.78,267);

insert into kolkata values(3,'AMRI HOSPITAL','16 17,JC BLOCK LANE,BROADWAY ROAD,OPPOSITE SALT LAKE,SECTOR III,BIDHANNAGAR,KOLKATA,WEST BENGAL-700098',3366063,72,9,70.11,301);

insert into kolkata values(4,'BELEGHATA ID AND BG HOSPITAL','57,BELEGHATA MAIN RD, SUBHAS SAROBAR PARK,PHOOL BAGAN,BELEGHATA,KOLKATA,WEST BENGAL-700010',33303200,115,9,77.23,356);
''')
conn.commit()

c.executescript('''insert into chennai values(1,'Rajiv Gandhi Government General Hospital','GH Post Office, 3, Poonamallee High Road, Near Chennai Central, near Park Town, Chennai, Tamil Nadu 600003',04425305000,1600,800,81,315);

insert into chennai values(2,' HOSPITAL','822, Poonamallee High Rd, near Ega Theatre, Kilpauk, Chennai, Tamil Nadu 600010',04426412979,500,100,70.35,153);

''')
conn.commit()

c.executescript('''INSERT INTO CASES VALUES(1,'DELHI',359000,327000,6312);
INSERT INTO CASES VALUES(2,'MUMBAI',1654028,1478496,43463);
INSERT INTO CASES VALUES(3,'KOLKATA',157000,144000,3074);
INSERT INTO CASES VALUES(4,'CHENNAI',397800,314700,6604);

''')
conn.commit()

c.executescript('''INSERT INTO PRICES VALUES(1,'Rs8000-Rs10000','Rs15000-Rs18000','Rs13000-Rs15000');
INSERT INTO PRICES VALUES(2,'Rs4000-Rs6000','Rs9000-Rs11000','Rs7500-Rs9500');
INSERT INTO PRICES VALUES(3,'Rs3000-Rs5000','Rs10000-Rs15000','Rs9000-Rs13500');
INSERT INTO PRICES VALUES(4,'Rs3000-Rs5000','Rs12000-Rs15000','Rs8000-Rs12000' );
''')
conn.commit()
"""
realp=c.execute('SELECT PASSWD from user_data;').fetchone()

def home():
    print('''#======================================================================================================#
#   /$$$$$$$$                                            /$$$$$$                      /$$       /$$    #
#  |__  $$__/                                           /$$__  $$                    |__/      | $$    #
#     | $$  /$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$    /$$/$$  /$$$$$$$    #
#     | $$ /$$__  $$|____  $$ /$$_____/ /$$__  $$      | $$       /$$__  $$|  $$  /$$/ $$ /$$__  $$    #
#     | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$$$      | $$      | $$  \ $$ \  $$/$$/| $$| $$  | $$    #
#     | $$| $$      /$$__  $$| $$      | $$_____/      | $$    $$| $$  | $$  \  $$$/ | $$| $$  | $$    #
#     | $$| $$     |  $$$$$$$|  $$$$$$$|  $$$$$$$      |  $$$$$$/|  $$$$$$/   \  $/  | $$|  $$$$$$$    #
#     |__/|__/      \_______/ \_______/ \_______/       \______/  \______/     \_/   |__/ \_______/    #
#    ```````````````````````````````````````````````````````````````````````````````````````````````   #
#======================================================================================================#
''')
    print('INDIA')
    A=pd.read_sql('SELECT * FROM INDIA;',conn)
    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))


    e=input('''
                        +__________________________________________________+
                        |MAIN MENU                                         |            ********************
                        |                                                  |            *  h to home       *
                        |     1 >> SELECT CITY                             |            *  q to quit       *
                        |                                                  |            ********************
                        |     2 >> ADMIN (UPDATE INFO)                     |
                        +__________________________________________________+


SELECT YOUR ENTRY:''')
    if e=='1':
        showData()
    elif e=='2':
        admin()
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    else:
        print("INVALID INPUT.")
        os.system('cls')
        home()


def city():
    e=input('''
SELECT THE CITY:
1.DELHI                                                                                 ********************
2.MUMBAI                                                                                *  h to home       *
3.KOLKATA                                                                               *  q to quit       *
4.CHENNAI                                                                               ********************


:''')
    return e

def showData():
    e=city()
    if e=='1':
        table='delhi'
        name='Delhi'
        SNO='1'
        e=options(name,table,SNO)

    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
 
    elif e=='2':
        table='mumbai'
        name='Mumbai'
        SNO='2'
        e=options(name,table,SNO)


    elif e=='3':
        table='kolkata'
        name='Kolkata'
        SNO='3'
        e=options(name,table,SNO)

    elif e=='4':
        table='chennai'
        name='Chennai'
        SNO='4'
        e=options(name,table,SNO)

def options(name,table,SNO):
    e=input('''
1.BED RATES                                                                              ********************
2.CASES                                                                                  *  h to home       *
3.HOSPITAL INFORMATION                                                                   *  q to quit       *
                                                                                         ********************
:''')
    if e=='1':
        bedPrices(SNO)
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
        
 
    elif e=='2':
        dispCases(SNO)
    elif e== '3':
        e=hospitals(name,table,SNO)
    else:
        print('INVALID INPUT.')
        options(name,table)

def bedPrices(SNO):
    A=pd.read_sql('SELECT * FROM PRICES WHERE SNO={}; '.format(SNO),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
    e=input('''********************
*  h to home       *
*  q to quit       *
********************
:''')
    
    if e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
        
 

def dispCases(SNO):
    A=pd.read_sql('SELECT * FROM CASES WHERE SNO={};'.format(SNO),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
    e=input('''********************
*  h to home       *
*  q to quit       *
********************
:''')
    if e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()


def hospitals(name,table,SNO):
    print('Data per hospital')
    A=pd.read_sql('SELECT * FROM {}'.format(table),conn)
    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A)

    e=input('''
********************
*  h to home       *
*  q to quit       *
********************
:''')
    if e=='*':
        e=allHosp(table)

    elif e=='1':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        oneHosp(name,table)
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
        
 
    elif e=='2':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        oneHosp(name,table)

    elif e=='3':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        oneHosp(name,table)
        
    elif e=='4':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        oneHosp(name,table)
         
    else:
        print('INVALID INPUT.')
        e=hospitals(name,table,SNO)

def allHosp(table):
    
    A=pd.read_sql('SELECT * FROM {};'.format(table),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
    e=input('''********************
*  h to home       *
*  q to quit       *
********************
:''')


def oneHosp(disp,table):
    print('print info of {}'.format(disp))
    A=pd.read_sql("SELECT * FROM {} WHERE SNO=1;".format(table),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
    e=input('''********************
*  h to home       *
*  q to quit       *
********************
:''')
    if e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()


def admin():
    pswd=input('ENTER PASWORD: ')
    global realp
    if pswd==(str(realp[0])):
        adminAccess()
    else:
        print('ACCESS DENIED')
        admin()

def adminAccess():
    e=input('''
1.UPDATE DATA                                                                           ********************
2.CHANGE PASSWORD                                                                       *  h to home       *
                                                                                        *  q to quit       *
                                                                                        ********************

:''')
    if e=='1':
        updateData()
    elif e=='2':
        changePass()
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
       
 
    else:
        print('INVALID INPUT.')
        adminAccess()

def updateData():
    e=input('''
SELECT CITY:
1.DELHI                                                                                 ********************
2.MUMBAI                                                                                *  h to home       *
3.KOLKATA                                                                               *  q to quit       *
4.CHENNAI                                                                               ********************

:''')
    if e=='1':
        table='delhi'
        SNO='1'
        updateCity(table,SNO)
    elif e=='2':
        table='mumbai'
        SNO='2'
        updateCity(table,SNO)
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
     
 
    elif e=='3':
        table='kolkata'
        SNO='3'
        updateCity(table,SNO)
    elif e=='4':
        table='chennai'
        SNO='4'
        updateCity(table,SNO)
    else:
        print('INVALID INPUT.')
        updateData()

def updateCity(table,SNO):
    e=input('''
What to update:
1.Hospital info                                                                         ********************
2.Different bed prices                                                                  *  h to home       *
3.No. of cases                                                                          *  q to quit       *
                                                                                        ********************
:''')
    if e=='1':
        updateHosp(table)
    elif e=='2':
        updateBedPrices(table,SNO)
    elif e=='3':
        updateCases(table,SNO)
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
       
 
    else:
        print('INVALID INPUT.')
        updateCity(table)

def updateHosp(table):
    A=pd.read_sql('SELECT SNO,NAME_OF_HOSPITAL from {};'.format(table),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))

    e=input('''SELECT HOSPITAL(SNO.):''')
    if e=='1':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        updateDetails(name[0],table)
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
      
 
    elif e=='2':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        updateDetails(name[0],table)
    elif e=='3':
        name=c.execute('select NAME_OF_HOSPITAL from {};'.format(table)).fetchone()
        updateDetails(name[0],table)
    else:
        print('INVALID INPUT')
        updateHosp(table)

def updateDetails(name,table):
    e=input('''
WHAT TO UPDATE:
1.VACANT BEDS                                                                           ********************
2.TOTAL BEDS                                                                            *  h to home       *
3.RECOVERY RATE                                                                         *  q to quit       *
4.TOTAL DEATHS                                                                          ********************

:''')
    if e=='1':
        updateVacantBeds(name,table)
    elif e=='3':
        updateRecoveryRate(name,table)
    elif e=='4':
        updateTotalDeaths(name,table)
    elif e=='2':
        updateTotalBeds(name,table)
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
       
 
    else:
        print('INVALID INPUT')
        updateHosp(table)


def updateVacantBeds(name,table):
    print('CURRENT VALUE:')
    A=pd.read_sql('SELECT VACANT_BEDS from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    n=int(input('ENTER NEW VALUE:'))
    c.execute('UPDATE {} set VACANT_BEDS = {} WHERE NAME_OF_HOSPITAL={};'.format(table,n,name))
    conn.commit()
    print('CHANGES SAVED.')
    
    A=pd.read_sql('SELECT VACANT_BEDS from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    adminAccess()

def updateRecoveryRate(name,table):
    print('CURRENT VALUE:')
    A=pd.read_sql('SELECT RECOVERY_RATE from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    n=int(input('ENTER NEW VALUE:'))
    c.execute('UPDATE {} set RECOVERY_RATE = {} WHERE NAME_OF_HOSPITAL={};'.format(table,n,name))
    conn.commit()
    print('CHANGES SAVED.')
    
    A=pd.read_sql('SELECT TOTAL_DEATHS from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    adminAccess()

def updateTotalDeaths(name,table):
    print('CURRENT VALUE:')
    
    A=pd.read_sql('SELECT TOTAL_DEATHS from CASES WHERE NAME_OF_HOSPITAL={};'.format(name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    n=int(input('ENTER NEW VALUE:'))
    c.execute('UPDATE {} set TOTAL_DEATHS = {} WHERE NAME_OF_HOSPITAL={};'.format(table,n,name))
    conn.commit()
    print('CHANGES SAVED.')
    
    A=pd.read_sql('SELECT TOTAL_DEATHS from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    adminAccess()

def updateTotalBeds(name,table):
    print('CURRENT VALUE:')
    
    A=pd.read_sql('SELECT TOTAL_BEDS from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    n=int(input('ENTER NEW VALUE:'))
    c.execute('UPDATE {} set TOTAL_BEDS = {} WHERE NAME_OF_HOSPITAL={};'.format(table,n,name))
    conn.commit()
    print('CHANGES SAVED.')
    
    A=pd.read_sql('SELECT TOTAL_BEDS from {} WHERE NAME_OF_HOSPITAL={};'.format(table,name),conn)

    Width=os.get_terminal_size()
    pd.set_option('display.width',Width[0])
    print(A.to_string(index=False))
 
    adminAccess()

def updateBedPrices(table,SNO):
    e=input('''
UPDATE BED PRICES:
1.ISOLATION BEDS                                                                        ********************
2.ICU BEDS WITHOUT VENTILATOR                                                           *  h to home       *
3.ICU BEDS WITH VENTILATOR                                                              *  q to quit       *
                                                                                        ********************




:''')
    if e=='1':
        print('CURRENT VALUE:')
        
        A=pd.read_sql('SELECT ISOLATION_BEDS from PRICE WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        n=int(input('ENTER NEW VALUE:'))
        c.execute('UPDATE PRICE set ISOLATION_BEDS = {} WHERE SNO={};'.format(n,SNO))
        conn.commit()
        print('CHANGES SAVED.')
        
        A=pd.read_sql('SELECT ISOLATION_BEDS from PRICE WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        adminAccess()
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
        
 
    elif e=='2':
        print('CURRENT VALUE:')
        
        A=pd.read_sql('SELECT ICU_BEDS_WITHOUT_VENTILATOR from PRICE WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        n=int(input('ENTER NEW VALUE:'))
        c.execute('UPDATE PRICE set ICU_BEDS_WITHOUT_VENTILATOR = {} WHERE SNO= {};'.format(n,SNO))
        conn.commit()
        print('CHANGES SAVED.')
        
        A=pd.read_sql('SELECT ICU_BEDS_WITHOUT_VENTILATOR from PRICE WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        adminAccess()
    elif e=='3':
        print('CURRENT VALUE:')
        
        A=pd.read_sql('SELECT ICU_BEDS_WITH_VENTILATOR from PRICE WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        n=int(input('ENTER NEW VALUE:'))
        c.execute('UPDATE PRICE set ICU_BEDS_WITH_VENTILATOR = {} WHERE SNO={};'.format(n,SNO))
        conn.commit()
        print('CHANGES SAVED.')
        
        A=pd.read_sql('SELECT ICU_BEDS_WITH_VENTILATOR from PRICE WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        adminAccess()

    else:
        print('INVALID INPUT.')
        updateBedPrices()

def updateCases(table,SNO):
    e=input('''WHICH CASES:
1.TOTAL CASES                                                                           ********************
2.RECOVERED CASES                                                                       *  h to home       *
3.DEATHS                                                                                *  q to quit       *
                                                                                        ********************
:''')
    if e=='1':
        print('CURRENT VALUE:')
        
        A=pd.read_sql('SELECT TOTAL_CASES from CASES WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        n=int(input('ENTER NEW VALUE:'))
        c.execute('UPDATE CASES set TOTAL_CASES = {} WHERE SNO={};'.format(n,SNO))
        conn.commit()
        print('CHANGES SAVED.')
        
        A=pd.read_sql('SELECT TOTAL_CASES from CASES WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        adminAccess()
    
    elif e=='q':
        print("THANK YOU!!!!!")
        quit()
    elif e=='h':
        os.system('cls')
        home()
    
       
 
    elif e=='2':
        print('CURRENT VALUE:')
        
        A=pd.read_sql('SELECT RECOVERED_CASES from CASES WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        n=int(input('ENTER NEW VALUE:'))
        c.execute('UPDATE CASES set RECOVERED_CASES = {} WHERE SNO={};'.format(n,SNO))
        conn.commit()
        print('CHANGES SAVED.')
        
        A=pd.read_sql('SELECT RECOVERED_CASES from CASES WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        adminAccess()
    elif e=='3':
        print('CURRENT VALUE:')
        
        A=pd.read_sql('SELECT DEATHS from CASES WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        n=int(input('ENTER NEW VALUE:'))
        c.execute('UPDATE CASES set DEATHS = {} WHERE SNO={};'.format(n,SNO))
        conn.commit()
        print('CHANGES SAVED.')
        
        A=pd.read_sql('SELECT DEATHS from CASES WHERE SNO={};'.format(SNO),conn)

        Width=os.get_terminal_size()
        pd.set_option('display.width',Width[0])
        print(A.to_string(index=False))
 
        adminAccess()
    else:
        print('INVALID INPUT')
        updateCases(table,SNO)

def changePass():
    cp=input('ENTER CURRENT PASSWORD:')
    global realp
    
    if cp==str(realp[0]):
        np=str(input('ENTER NEW PASSWORD:'))
        c.execute('UPDATE user_data set PASSWD = "{}" where SNO = 1;'.format(np))
        conn.commit()
        realp=c.execute('SELECT PASSWD from user_data;').fetchone()
        print('PASSWORD CHANGED.')
        
        adminAccess()
    else:
        print('WRONG PASSWORD')
        changePass()

home()

c.close()

#MADE BY DEEPANSHU AND MANIYA OF XII-A