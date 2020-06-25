import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

pswd = 'December9_$'
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:{}@localhost:3306/ITOI_DB'.format(pswd),echo=True)
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

def getDBClass(tableName):
	if tableName == 'USER':
		dbClass = Base.classes.USER
	elif tableName == 'MEETING':
		dbClass = Base.classes.MEETING
	elif tableName == 'ATTENDEE':
		dbClass = Base.classes.ATTENDEE
	elif tableName == 'GOAL':
		dbClass = Base.classes.GOAL
	elif tableName == 'DECISION':
		dbClass = Base.classes.DECISION
	elif tableName == 'SKILL':
		dbClass = Base.classes.SKILL
	elif tableName == 'WEIGHT':
		dbClass = Base.classes.WEIGHT
	elif tableName == 'RATING':
		dbClass = Base.classes.RATING

	return dbClass




