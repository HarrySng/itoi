from dbSetup import dbClasses as db
from logic import user, meeting, goal, attendee


def showTable(table):
	tableClass = db.getDBClass(table)
	tableData = db.session.query(tableClass).all()
	for row in tableData:
		print(row.__dict__)
