#import sys
#sys.setdefaultencoding('utf8')
import pandas as pd


import urllib
import pyodbc
import sqlalchemy
import urllib

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


import csv

Base = declarative_base()

class vinho(Base):
	__tablename__ = 'wines'
	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	country = Column(String)
	description = Column(String)
	designation = Column(String)
	points = Column(Integer)
	price = Column(Integer)
	province = Column(String)
	region1 = Column(String)
	region2 = Column(String)
	tasterName = Column(String)
	tasterTwitterHandle = Column(String)
	title = Column(String)
	variety = Column(String)
	winery = Column(String)

	def __repr__(self):
		return "<vinho(id = '%d', country = '%s', description = '%s', designation = '%s', points = '%d', price = '%d', province = '%s', region1 = '%s', region2 = '%s', tasterName = '%s', tasterTwitterHandle = '%s', title = '%s', variety = '%s', winery = '%s')>" % (self.id, self.country, self.description, self.designation, self.points, self.price, self.province, self.region1, self.region2, self.tasterName, self.tasterTwitterHandle, self.title, self.variety, self.winery)


params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};Server=localhost;Database=vinhos;UID=superSA;PWD=senha12!;")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
Session = Session(bind=engine)

df = pd.read_csv('wine-reviews\winemag-data-130k-v2.csv')
print(df)

#df.fillna(0,inplace=True)
#for index, linha in df.iterrows():
#	vinhoObj = vinho(country = linha['country'], description = linha['description'], designation = linha['designation'], points = linha['points'], price = linha['price'], province = linha['province'],
#				region1 = linha['region_1'],region2 = linha['region_2'], tasterName = linha['taster_name'], tasterTwitterHandle = linha['taster_twitter_handle'], title = linha['title'], variety = linha['variety'], winery = linha['winery'])
#	Session.add(vinhoObj)
#   #print(row['Id'])
#   #break
#
#Session.commit()

#with open('wine-reviews\winemag-data_first150k.csv', 'r') as csvfile:
#	fieldNames = ['id', 'country', 'description', 'designation', 'points', 'price', 'province', 'region1', 'region2', 'tasterName', 'tasterTwitterHandle', 'title', 'variety', 'winery']
#	spamreader = csv.DictReader(csvfile,fieldnames=fieldNames,delimiter=',', dialect=csv.excel,quoting=csv.QUOTE_NONE)
#	for linha in spamreader:
#
#		#print(int(linha['price'])
#		print(linha)
#
#		#Session.commit()
#		#print(Session.new)
#
#try:
#except IntegrityError as error:
#	print('Erro de integridade')
#
