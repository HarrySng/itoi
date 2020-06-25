from dbSetup import dbClasses as db

def createGoal(goalName, meetingName, idDecided = 0):
	goalClass = db.getDBClass('GOAL')
	meetingClass = db.getDBClass('MEETING')
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	newGoal = goalClass(MEETING_ID = meetingID, GOAL_NAME = goalName, IS_DECIDED = idDecided)
	db.session.add(newGoal)
	db.session.commit()

def decideGoal(goalName, meetingName):
	"""
	Set goal status to 1
	"""
	goalClass = db.getDBClass('GOAL')
	meetingClass = db.getDBClass('MEETING')
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	db.session.query(goalClass).filter(goalClass.MEETING_ID == meetingID).filter(goalClass.GOAL_NAME == goalName).update({goalClass.IS_DECIDED: 1})
	db.session.commit()

def deleteGoal(goalName, meetingName):
	goalClass = db.getDBClass('GOAL')
	meetingClass = db.getDBClass('MEETING')
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	db.session.query(goalClass).filter(goalClass.MEETING_ID == meetingID).filter(goalClass.GOAL_NAME == goalName).delete()
	b.session.commit()