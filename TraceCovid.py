import sqlite3
import pandas as pd
import os


#main menu
def home():
	print('''				#======================================================================================================#
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


#selecting city
def city():
	e=input('''
SELECT THE CITY:
1.DELHI                                                                                 ********************
2.MUMBAI                                                                                *  h to home       *
3.KOLKATA                                                                               *  q to quit       *
4.CHENNAI                                                                               ********************


:''')
	return e


#Data Display
def showData():
	e=city()
	if e=='1':
		table='delhi'							#for refrencing to the database
		name='Delhi'							#for refrencing to the database
		SNO='1'									#for refrencing to the database
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


#Options to be displayed
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


#Displaying bed prices
def bedPrices(SNO):
	print("MAX PRICE:")
	A=pd.read_sql('SELECT * FROM PRICES WHERE SNO={};'.format(SNO),conn)

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
	
		
 
#displaying no. of cases
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


#displaying information about hospitals
def hospitals(name,table,SNO):
	print('Data per hospital')
	A=pd.read_sql('SELECT * FROM {}'.format(table),conn)
	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	e=input('''
********************
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
		 
	else:
		print('INVALID INPUT.')
		e=hospitals(name,table,SNO)


#for Admin access
def admin():
	pswd=input('ENTER PASWORD: ')
	global realp
	if pswd==(str(realp[0])):
		adminAccess()
	else:
		print('ACCESS DENIED')
		admin()

#Options for admin to do
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


#Changing the data
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


#Change data per city
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


#change data of hospitals
def updateHosp(table):
	A=pd.read_sql('SELECT SNO,NAME_OF_HOSPITAL from {};'.format(table),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	e=input('''SELECT HOSPITAL(SNO.):''')
	if e=='1':
		name=c.execute('select NAME_OF_HOSPITAL from ?;',(table)).fetchone()
		updateDetails(name[0],table)
	
	elif e=='q':
		print("THANK YOU!!!!!")
		quit()
	elif e=='h':
		os.system('cls')
		home()
	
	  
 
	elif e=='2':
		name=c.execute('select NAME_OF_HOSPITAL from ?;',(table)).fetchone()
		updateDetails(name[0],table)
	elif e=='3':
		name=c.execute('select NAME_OF_HOSPITAL from ?;',(table)).fetchone()
		updateDetails(name[0],table)
	else:
		print('INVALID INPUT')
		updateHosp(table)


#change data regarding beds
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


#change no. of vacant beds per hospital
def updateVacantBeds(name,table):
	print('CURRENT VALUE:')
	A=pd.read_sql('SELECT VACANT_BEDS from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))
 
	n=int(input('''ENTER NEW VALUE:'''))
	c.execute('UPDATE ? set VACANT_BEDS = ? WHERE NAME_OF_HOSPITAL="?";',(table,n,name))
	conn.commit()
	print('CHANGES SAVED.')
	
	A=pd.read_sql('SELECT VACANT_BEDS from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))
 
	adminAccess()


#change data of recovery rate per hospital
def updateRecoveryRate(name,table):
	print('CURRENT VALUE:')
	A=pd.read_sql('SELECT RECOVERY_RATE from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))
 
	n=int(input('ENTER NEW VALUE:'))
	c.execute('UPDATE ? set RECOVERY_RATE = ? WHERE NAME_OF_HOSPITAL="?";',(table,n,name))
	conn.commit()
	print('CHANGES SAVED.')

	A=pd.read_sql('SELECT TOTAL_DEATHS from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	adminAccess()


#change data of total deaths per hospital
def updateTotalDeaths(name,table):
	print('CURRENT VALUE:')

	A=pd.read_sql('SELECT TOTAL_DEATHS from CASES WHERE NAME_OF_HOSPITAL="{}";'.format(name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	n=int(input('ENTER NEW VALUE:'))
	c.execute('UPDATE ? set TOTAL_DEATHS = ? WHERE NAME_OF_HOSPITAL="?";',(table,n,name))
	conn.commit()
	print('CHANGES SAVED.')

	A=pd.read_sql('SELECT TOTAL_DEATHS from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	adminAccess()


#change data of total beds per hospital
def updateTotalBeds(name,table):
	print('CURRENT VALUE:')
	
	A=pd.read_sql('SELECT TOTAL_BEDS from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	n=int(input('ENTER NEW VALUE:'))
	c.execute('UPDATE ? set TOTAL_BEDS = ? WHERE NAME_OF_HOSPITAL="?";',(table,n,name))
	conn.commit()
	print('CHANGES SAVED.')
	
	A=pd.read_sql('SELECT TOTAL_BEDS from {} WHERE NAME_OF_HOSPITAL="{}";'.format(table,name),conn)

	Width=os.get_terminal_size()
	pd.set_option('display.width',Width[0])
	print(A.to_string(index=False))

	adminAccess()

#change data of bed prices per city
def updateBedPrices(table,SNO):
	e=input('''
UPDATE BED PRICES:
1.ISOLATION BEDS                                                                        ********************
2.ICU BEDS WITHOUT VENTILATOR                                                           *  h to home       *
3.ICU BEDS WITH VENTILATOR                                                              *  q to quit       *
																						********************


:''')
	if e=='1':
		print('CURRENT MAX PRICE:')

		A=pd.read_sql('SELECT ISOLATION_BEDS from PRICES WHERE SNO={};'.format(SNO),conn)

		Width=os.get_terminal_size()
		pd.set_option('display.width',Width[0])
		print(A.to_string(index=False))

		n=int(input('MAX PRICE: '))
		c.execute('UPDATE PRICES set ISOLATION_BEDS = ? WHERE SNO=?;',(n,SNO))
		conn.commit()
		print('CHANGES SAVED.')

		A=pd.read_sql('SELECT ISOLATION_BEDS from PRICES WHERE SNO={};'.format(SNO),conn)

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
		print('CURRENT MAX PRICE:')
		
		A=pd.read_sql('SELECT ICU_BEDS_WITHOUT_VENTILATOR from PRICES WHERE SNO={};'.format(SNO),conn)

		Width=os.get_terminal_size()
		pd.set_option('display.width',Width[0])
		print(A.to_string(index=False))
 
		n=int(input('MAX PRICE: '))
		c.execute('UPDATE PRICES set ICU_BEDS_WITHOUT_VENTILATOR = ? WHERE SNO= ?',(n,SNO))
		conn.commit()
		print('CHANGES SAVED.')
		
		A=pd.read_sql('SELECT ICU_BEDS_WITHOUT_VENTILATOR from PRICES WHERE SNO={};'.format(SNO),conn)

		Width=os.get_terminal_size()
		pd.set_option('display.width',Width[0])
		print(A.to_string(index=False))
 
		adminAccess()
	elif e=='3':
		print('CURRENT MAX PRICE:')
		
		A=pd.read_sql('SELECT ICU_BEDS_WITH_VENTILATOR from PRICES WHERE SNO={};'.format(SNO),conn)

		Width=os.get_terminal_size()
		pd.set_option('display.width',Width[0])
		print(A.to_string(index=False))
 
		n=int(input('MAX PRICE: '))
		c.execute('UPDATE PRICES set ICU_BEDS_WITH_VENTILATOR = ? WHERE SNO=?;',(n,SNO))
		conn.commit()
		print('CHANGES SAVED.')
		
		A=pd.read_sql('SELECT ICU_BEDS_WITH_VENTILATOR from PRICES WHERE SNO={};'.format(SNO),conn)

		Width=os.get_terminal_size()
		pd.set_option('display.width',Width[0])
		print(A.to_string(index=False))
 
		adminAccess()

	else:
		print('INVALID INPUT.')
		updateBedPrices()

#change data of no. of cases
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
		c.execute('UPDATE CASES set TOTAL_CASES = ? WHERE SNO=?;',(n,SNO))
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
		c.execute('UPDATE CASES set RECOVERED_CASES = ? WHERE SNO=?;',(n,SNO))
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
		c.execute('UPDATE CASES set DEATHS = ? WHERE SNO=?;',(n,SNO))
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


#Changing the admin password
def changePass():
	cp=input('ENTER CURRENT PASSWORD:')
	global realp
	
	if cp==str(realp[0]):
		np=str(input('ENTER NEW PASSWORD:'))
		c.execute('UPDATE user_data set PASSWD = "?" where SNO = 1;',(np))
		conn.commit()
		realp=c.execute('SELECT PASSWD from user_data;').fetchone()
		print('PASSWORD CHANGED.')
		
		adminAccess()
	else:
		print('WRONG PASSWORD')
		changePass()


#__main__


#connection to sqlite
conn=sqlite3.connect('TraceCovid.db')


#cursor
c=conn.cursor()


#tables script
c.executescript('''Create table if not exists delhi (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (95),CONTACT  int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists mumbai (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (115),CONTACT int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists kolkata (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (115),CONTACT int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists chennai (SNO integer , NAME_OF_HOSPITAL varchar(85),ADDRESS_OF_HOSPITAL varchar (115),CONTACT int(35),TOTAL_BEDS int (37),VACANT_BEDS int (37),RECOVERY_RATE float ,TOTAL_DEATHS int(27));

create table if not exists CASES(SNO int,NAME_OF_CITY varchar(17),TOTAL_CASES INT(37),RECOVERED_CASES INT(40),DEATHS INT(35));

CREATE TABLE IF NOT EXISTS PRICES(SNO INT,ISOLATION_BEDS integer,ICU_BEDS_WITH_VENTILATOR integer,ICU_BEDS_WITHOUT_VENTILATOR integer);

create table if not exists INDIA(TOTAL_CASES varchar,RECOVERED varchar,DEATHS varchar);

create table if not exists user_data(SNO int, PASSWD varchar(30) default'000');
''')
conn.commit()


#password
realp=c.execute('SELECT PASSWD from user_data;').fetchone()


home()


c.close()


#MADE BY DEEPANSHU AND MANIYA OF XII-A
