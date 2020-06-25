# Meeting process

```python
meetingName = "Kickoff Meeting"
goalName = "To invest?"
```

## Create new meeting and goal
```python
meeting.createMeeting(meetingName)
goal.createGoal(goalName, meetingName)
```

## Add Users
```python
for all users:
	user.addUser("userName", "password", isManager = 1)
```

## Add attendees to active meeting
```python
for all users:
	attendee.manageAttendee(meetingName, "userName")
```

## Add skills required for meeting
```python
for all skills:
	skill.manageSkill("skillName", meetingName)
```

## Vote on the goal
```python
for all users:
	vote.vote(goalName, 1/0, "userName")
```

## Rate all Attendees
```python
for all users:
	rating.rate([10,6,5,2], "skillName", "userName")
```

## Collect all votes and the ratings
```python
votes = vote.collectVotes(goalName, meetingName)
ratings = rating.collectRatings(meetingName)
```

## Show final decision
```python
def finalDecision(): 
	# see parent logic
```