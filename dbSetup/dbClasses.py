import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

pswd = 'December9_$'
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:{}@localhost:3306/ITOI_DB'.format(pswd),echo=True)
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

def getDBClass(tableName):
	if tableName == 'ORG':
		dbClass = Base.classes.ORG
	elif tableName == 'MANAGER':
		dbClass = Base.classes.MANAGER
	elif tableName == 'USER':
		dbClass = Base.classes.USER
	elif tableName == 'MEETING':
		dbClass = Base.classes.MEETING
	elif tableName == 'ATTENDEE':
		dbClass = Base.classes.ATTENDEE
	elif tableName == 'GOAL':
		dbClass = Base.classes.GOAL
	elif tableName == 'VOTE':
		dbClass = Base.classes.VOTE
	elif tableName == 'SKILL':
		dbClass = Base.classes.SKILL
	elif tableName == 'WEIGHT':
		dbClass = Base.classes.WEIGHT
	elif tableName == 'RATING':
		dbClass = Base.classes.RATING

	return dbClass




