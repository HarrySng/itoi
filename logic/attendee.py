from dbSetup import dbClasses as db

attendeeClass = db.getDBClass('ATTENDEE')
meetingClass = db.getDBClass('MEETING')
userClass = db.getDBClass('USER')

def manageAttendee(meetingName, userName, add = True):
	"""
	Add or remove an attendee from a meeting
	"""
	# Get meeting ID by filtering on meeting name
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	userID = db.session.query(userClass).filter(userClass.USERNAME == userName)[0].ID
	# Insert or delete attendee
	if add:
		newAttendee = attendeeClass(MEETING_ID = meetingID, USER_ID = userID)
		db.session.add(newAttendee)
	else:
		db.session.query(attendeeClass).filter(attendeeClass.MEETING_ID == meetingID).filter(attendeeClass.USER_ID == userID).delete()
	db.session.commit()