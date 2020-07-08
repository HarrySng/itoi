from dbSetup import dbClasses as db
import string
import random

orgClass = db.getDBClass('ORG')

def keyGen(size=30, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def addOrg(orgName):
	key = keyGen()
	newOrg = orgClass(ORG_NAME = orgName, ORG_KEY = key)
	db.session.add(newOrg)
	db.session.commit()
	print("New Org '{}' has been added with key '{}'. Save this key for future purposes.".format(orgName, key))

#ONC -------  H7E9WTI0W705UCC8WL7031VNO8XUIO