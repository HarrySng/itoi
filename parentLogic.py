from dbSetup import dbClasses as db
from logic import user, meeting, goal, attendee

classDict = {}
for table in ['ORG', 'MANAGER', 'USER', 'MEETING', 'ATTENDEE', 'GOAL', 'VOTE', 'SKILL', 'RATING']:
	classDict[table] = db.getDBClass(table)

# Get ORGS to show on orgPage
def getOrgs():
	orgTable = db.session.query(classDict['ORG']).all()
	orgs = []
	for row in orgTable:
		orgs.append(row.ORG_NAME)
	return orgs

# Get dashboard info to show on dashboard.html when user logs in
def getDashboard(orgID, mngrID):
	mID = db.session.query(classDict['MANAGER']).filter(classDict['MANAGER'].ORG_ID == orgID).filter(classDict['MANAGER'].USERNAME == mngrID)[0].ID
	# This is the primary key of manager table
	# All data to display on dashboard will be pulled from other tables using this FK


def showTable(table):
	tableData = db.session.query(classDict[table]).all()
	for row in tableData:
		print(row.__dict__)

#votes = vote.collectVotes(goalName, meetingName, votes)
#ratings = rating.collectRatings(meetingName)
def finalDecision(goalName, meetingName, votes, ratings): # fetch all votes for this meeting
	
    
    meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	qAttendees = db.session.query(attendeeClass).filter(attendeeClass.MEETING_ID == meetingID).all()
	users = {}
	
    for row in qAttendees:
		userID = row.USER_ID
		userName = db.session.query(userClass).filter(userClass.ID == userID)[0].USERNAME
		users[userID] = userName
	userIDs = list(users)
	decisionDict = {}
    
	for userID in userIDs:
		decisionDict[users[userID]] = ["Yes" if votes[userID] == 1 else "No", ratings[userID]]
	print("The original decision for the goal '{}' taken in '{}' meeting is:\n".format(goalName, meetingName))
	
    for key in decisionDict:
		print("{} voted {}.\n".format(key, decisionDict[key][0]))
	print("The original decision is {} percent Yes and {} percent No.".format(round((list(votes.values()).count(1)/len(votes))*100,2), round((list(votes.values()).count(0)/len(votes))*100,2)))
	yes = []
	no = []
	
    for element in list(decisionDict.values()):
		if element[0] == 'Yes':
			yes.append(element[1])
		else:
			no.append(element[1])
	weightedYes = round(sum(yes)/len(ratings)*10,2)
	weightedNo = round(sum(no)/len(ratings)*10,2)
	uncertainty = round(100-(weightedYes+ weightedNo),2)
	print("##### WEIGHTED DECISION #####")
	print("The weighted decision is {} percent Yes and {} percent No with an uncertainty of {} percent.".format(weightedYes, weightedNo, uncertainty))
	
    if weightedYes == max(weightedYes, weightedNo, uncertainty):
		finalAnswer = "GO FOR IT!"
	elif weightedNo == max(weightedYes, weightedNo, uncertainty):
		finalAnswer = "a NO GO!"
	elif uncertainty == max(weightedYes, weightedNo, uncertainty):
		finalAnswer = "too uncertain. Please reconsider!"
	print("The team's final decision is {}.".format(finalAnswer))
