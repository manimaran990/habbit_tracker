import sys
import datetime
import json
from collections import OrderedDict


CURRENT_DATE = datetime.datetime.now().strftime("%d-%h-%Y %H:%M:%S")

class NewHabbit(object):

	def __init__(self,name):
		self.habbit_name = name
		self.created_date = CURRENT_DATE
		self.data = {}		
		self.data['habbit_name'] = name
		self.data['created_date'] = CURRENT_DATE
		self.data['alldates'] = OrderedDict()


	def set_status(self, done_date, desc):
		self.data['alldates'][done_date] = desc

	def get_status(self):
		if len(self.data) == 0:
			print("No status found")
		else:			
			for k in self.data['alldates'].keys():
				print("habbit: {} \ndate: {}  \ndesc: {} \nTotal Days: {}".format(self.habbit_name, k, 
					self.data['alldates'][k], len(self.data['alldates'])))


	def have_status_data(self):
		return len(self.data) > 0

	def __str__(self):
		return "{} : created on {}".format(self.habbit_name.capitalize(), self.created_date)

	def getjson(self):		
		return self.data

	#save to collection
	def saveData(self, colname):
		colname.insert_one(self.data)

	#view data from collection
	def viewData(self, colname):
		for habbit in colname.find():
			print(habbit)
