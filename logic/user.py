from dbSetup import dbClasses as db

userClass = db.getDBClass('USER')

def addUser(userName, pswd, isManager = 0):
	newUser = userClass(USERNAME = userName, PASSWORD = pswd, IS_MANAGER = isManager)
	db.session.add(newUser)
	db.session.commit()

def changeManagerStatus(userName, isManager):
	"""
	Make a user manager. Or demote a user from mamager position.
	"""
	db.session.query(userClass).filter(userClass.USERNAME == userName).update({userClass.IS_MANAGER: isManager})
	db.session.commit()

def changePassword(userName, pswd):
	db.session.query(userClass).filter(userClass.USERNAME == userName).update({userClass.PASSWORD: pswd})
	db.session.commit()