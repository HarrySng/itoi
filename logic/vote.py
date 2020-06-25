from dbSetup import dbClasses as db

voteClass = db.getDBClass('VOTE')
userClass = db.getDBClass('USER')
meetingClass = db.getDBClass('MEETING')
goalClass = db.getDBClass('GOAL')
attendeeClass = db.getDBClass('ATTENDEE')

def vote(goalName, decision, userName):
	meetingID = db.session.query(meetingClass).filter(meetingClass.IS_ACTIVE == 1)[0].ID # Active meeting
	goalID = db.session.query(goalClass).filter(goalClass.GOAL_NAME == goalName).filter(goalClass.MEETING_ID == meetingID)[0].ID
	userID = db.session.query(userClass).filter(userClass.USERNAME == userName)[0].ID
	newDecision = voteClass(DECISION = decision, GOAL_ID = goalID, USER_ID = userID)
	db.session.add(newDecision)
	db.session.commit()

def collectVotes(goalName, meetingName):
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	goalID = db.session.query(goalClass).filter(goalClass.GOAL_NAME == goalName).filter(goalClass.MEETING_ID == meetingID)[0].ID
	qVotes = db.session.query(voteClass).filter(voteClass.GOAL_ID == goalID).all()
	# Check if all voted
	qAttendees = db.session.query(attendeeClass).filter(attendeeClass.MEETING_ID == meetingID).all()
	if len(qVotes) != len(qAttendees):
		return "Everyone has not voted on this goal. Please vote to continue."
	# Now who voted what
	votes = {}
	for row in qVotes:
		votes[row.USER_ID] = row.DECISION
	return votes
