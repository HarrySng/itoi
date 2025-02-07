from dbSetup import dbClasses as db

userClass = db.getDBClass('USER')

# Everything should happen within the ORG

def addUser(userName, pswd, email, orgName, isManager = 0):

	newUser = userClass(USERNAME = userName, PASSWORD = pswd, EMAIL_ID = email, IS_MANAGER = isManager)
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

def deleteUser(userName, pswd):
	db.session.query(userClass).filter(userClass.USERNAME == userName).delete()
	db.session.commit()

