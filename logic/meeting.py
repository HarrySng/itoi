from dbSetup import dbClasses as db

meetingClass = db.getDBClass('MEETING') # Create class


def createMeeting(meetingName, isActive = 1):
	if isActive == 1: # If activating this meeting, make all others inactive
		db.session.query(meetingClass).update({meetingClass.IS_ACTIVE: 0})
	newMeeting = meetingClass(MEETING_NAME = meetingName, IS_ACTIVE = isActive) # Insert new meeting
	db.session.add(newMeeting) # Add it to db
	db.session.commit() # commit

def endAllMeetings():
	db.session.query(meetingClass).update({meetingClass.IS_ACTIVE: 0})

def startMeeting(meetingName):
	db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == "testMeeting").update({meetingClass.IS_ACTIVE: 1})
	# Above: Filter the query based on meeting name then activate the active flag
	db.session.commit() # commit