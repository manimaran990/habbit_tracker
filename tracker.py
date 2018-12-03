'''
	Simple habbit tracker application
	by: manimaran G
	date: 02-12-2018
'''
import sys
import datetime
import json
from collections import OrderedDict
from NewHabbit import NewHabbit
import pymongo

myclient = pymongo.MongoClient("mongodb://m4n1g:DragonBall9@ds249092.mlab.com:49092/blog_db")
mydb = myclient["blog_db"]
habbit_col = mydb["habbits_col"]


CURRENT_DATE = datetime.datetime.now().strftime("%d-%h-%Y %H:%M:%S")


if __name__ == '__main__':

	#list to store objects
	HABBIT_OBJECTS = []

	while True:
		option = int(input('''1. Update Habbit\n2. View status\n3. New Habbit\n4. Exit\n5. Save to DB\n6. View DB\n'''))				

		#if input is 3 or more exit
		if option ==4:
			print("Bye..")
			sys.exit(0)

		#create new habbit object
		elif option == 3:						
			hb_name = input("Enter habbit name: ")
			habbit = NewHabbit(hb_name)
			HABBIT_OBJECTS.append(habbit)

		elif option	== 2:

			if len(HABBIT_OBJECTS) > 0:
				for habbit in HABBIT_OBJECTS:
					habbit.get_status()
			else:
				print("No status data found")

		#track habbits
		elif option == 1:
			if len(HABBIT_OBJECTS) == 0:
				print("No habbits found!!")
			else:	
				print("List of Habbits")			
				for habbit in HABBIT_OBJECTS:
					print(habbit)
					status = input("Did you completed it today? (y/n) ")
					if status.lower() == 'y':
						comment = input("Any comments ? ")						
						habbit.set_status(CURRENT_DATE, comment)
					else:
						continue					

		elif option == 5:
			for habbit in HABBIT_OBJECTS:				
				habbit.saveData(habbit_col)				

		elif option == 6:
			for habbit in HABBIT_OBJECTS:				
				habbit.viewData(habbit_col)








