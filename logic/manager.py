from dbSetup import dbClasses as db

managerClass = db.getDBClass('MANAGER')
orgClass = db.getDBClass('ORG')


def addManager(userName, pswd, email, orgID):
	newManager = managerClass(USERNAME = userName, PASSWORD = pswd, EMAIL_ID = email, ORG_ID = orgID)
	db.session.add(newManager)
	db.session.commit()
