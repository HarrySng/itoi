# Meeting process

# Remove pass from dbclass

## Workflow
1. Selecting the Org (db: ORG, itoi: orgPage(), logic: org.py, parent: , ui:org.html, forms: NA)
	User selects an Org from a dropdown and clicks on Submit
User gets redirected to the Login page
2. Login (db: , itoi: , logic: , parent: , ui:, forms: )
	Get OrgID from step 1
	User enters ID, password and key
	Check on existing ID, and key WITHIN org and verify password
	If checks pass:
		Run a function getDashboard (imported from parentLogic). Pulls all info to display on dashboard
		Redirect user to dashboard
	If User does not exist, User clicks on Hyperlink that leads to signup page
3. Signup (db: , itoi: signup(), logic: , parent: , ui: signup.html,forms: signupForm)
	Get OrgID from step 1
	User enters ID, password, confirm password, email, key
	Check on existing ID, email and key WITHIN org
	If checks pass:
		Inser SQL, redirect to login page
4. Dashboard (db: , itoi: , logic: , parent: , ui:, forms: )
