from dbSetup import dbClasses as db
import numpy as np

ratingClass = db.getDBClass('RATING')
userClass = db.getDBClass('USER')
meetingClass = db.getDBClass('MEETING')
skillClass = db.getDBClass('SKILL')
attendeeClass = db.getDBClass('ATTENDEE')

def getRatingUserList():
	meetingID = db.session.query(meetingClass).filter(meetingClass.IS_ACTIVE == 1)[0].ID # Active meeting
	qAttendee = db.session.query(attendeeClass).filter(attendeeClass.MEETING_ID == meetingID).all() # Get attendees of meeting
	attendees = []
	for row in qAttendee:
		attendees.append(row.USER_ID) # Get User IDs of attendees
	# Now get their usernames to print out. These will be used to rate them in order in the next function
	qUsers = db.session.query(userClass).filter(userClass.ID.in_(attendees)).all()
	userNames = []
	for row in qUsers:
		userNames.append(row.USERNAME)
	return userNames

def rate(ratingList, skillName, ratingBy): # Not including meeting as active meeting should be selected by default
	
	meetingID = db.session.query(meetingClass).filter(meetingClass.IS_ACTIVE == 1)[0].ID
	userIDBy = db.session.query(userClass).filter(userClass.USERNAME == ratingBy)[0].ID
	skillID = db.session.query(skillClass).filter(skillClass.SKILL_NAME == skillName)[0].ID
	userList = getRatingUserList()
	ratingDict = dict(zip(userList, ratingList))

	for key in ratingDict:
		userIDFrom = db.session.query(userClass).filter(userClass.USERNAME == key)[0].ID
		newRating = ratingClass(RATING = ratingDict[key], SKILL_ID = skillID, RATING_FOR = userIDFrom, RATING_BY = userIDBy)
		db.session.add(newRating)
	db.session.commit()

def collectRatings(meetingName):
	"""
	Logic
		get active meeting. Get skills assigned to meeting. Get skill IDs.
		Match number of actual given ratings to total num of ratings required. Stop if not everyone rated.
		Get userIDs of attendees. For each userID, get the rating assigned for each skill in current meeting.
		Average the ratings and return
	"""
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID # active meeting
	qSkills = db.session.query(skillClass).filter(skillClass.MEETING_ID == meetingID).all() # Skills assigned to meeting
	skillIDs = []
	for row in qSkills:
		skillIDs.append(row.ID)
	qAttendees = db.session.query(attendeeClass).filter(attendeeClass.MEETING_ID == meetingID).all() # Number of attendees
	reqRatings = len(skillIDs)*len(qAttendees)*len(qAttendees) # Total ratings that should be in table
	qRatings = db.session.query(ratingClass).filter(ratingClass.SKILL_ID.in_(skillIDs)).all()
	if reqRatings != len(qRatings):
		return "All people have not rated. Please rate to continue"
	# Now get the ratings for each person and average them
	userIDs = []
	for row in qAttendees:
		userIDs.append(row.USER_ID)
	avgRatings = {}
	for userID in userIDs:
		qUserRatings = db.session.query(ratingClass).filter(ratingClass.RATING_FOR == userID).filter(ratingClass.SKILL_ID.in_(skillIDs)).all()
		userRating = []
		for row in qUserRatings:
			userRating.append(row.RATING)
		avgRatings[userID] = round(np.mean(userRating),2)
	return avgRatings

