from dbSetup import dbClasses as db

goalClass = db.getDBClass('GOAL')
meetingClass = db.getDBClass('MEETING')

def createGoal(goalName, meetingName):
	
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	newGoal = goalClass(MEETING_ID = meetingID, GOAL_NAME = goalName)
	db.session.add(newGoal)
	db.session.commit()

def deleteGoal(goalName, meetingName):
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	db.session.query(goalClass).filter(goalClass.MEETING_ID == meetingID).filter(goalClass.GOAL_NAME == goalName).delete()
	b.session.commit()
