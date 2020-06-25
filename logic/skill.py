from dbSetup import dbClasses as db

skillClass = db.getDBClass('SKILL')
meetingClass = db.getDBClass('MEETING')

def manageSkill(skillName, meetingName, add = True):
	meetingID = db.session.query(meetingClass).filter(meetingClass.MEETING_NAME == meetingName)[0].ID
	if add:
		newSkill = skillClass(MEETING_ID = meetingID, SKILL_NAME = skillName)
		db.session.add(newSkill)
	else:
		db.session.query(skillClass).filter(skillClass.MEETING_ID == meetingID).filter(skillClass.SKILL_NAME == skillName).delete()
	db.session.commit()

