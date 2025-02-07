import sys
import mysql.connector
from mysql.connector import Error

def create_itoi_db(pswd):
    connection = mysql.connector.connect(
        host='localhost',
        database='ITOI_DB',
        user='root',
        password=pswd)

    queryList = [
    """
    CREATE TABLE ORG (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ORG_NAME VARCHAR(100) NOT NULL UNIQUE,
    ORG_KEY VARCHAR(255) NOT NULL UNIQUE);
    """,
    """
    CREATE TABLE MANAGER (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    USERNAME VARCHAR (50) NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL,
    EMAIL_ID VARCHAR(100) NOT NULL,
    ORG_ID INT,
    INDEX IND_ORG_MANAGER (ORG_ID),
    FOREIGN KEY (ORG_ID) REFERENCES ORG(ID));
    """,
    """
    CREATE TABLE USER (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    USERNAME VARCHAR(50) NOT NULL, # Handle uniqueness of username within org during runtime
    PASSWORD VARCHAR(255) NOT NULL, 
    EMAIL_ID VARCHAR(100) NOT NULL,
    ORG_ID INT,
    INDEX IND_ORG_USER (ORG_ID),
    FOREIGN KEY (ORG_ID) REFERENCES ORG(ID));
    """,
    """
    CREATE TABLE MEETING (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    MEETING_NAME VARCHAR(100) NOT NULL,
    IS_ACTIVE BOOLEAN DEFAULT FALSE,
    ORG_ID INT,
    INDEX IND_ORG_MEETING (ORG_ID),
    FOREIGN KEY (ORG_ID) REFERENCES ORG(ID));
    """,
    """
    CREATE TABLE ATTENDEE (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    MEETING_ID INT,
    USER_ID INT, # Handle during runtime - correct user gets added (multiple usernames across orgs)
    INDEX IND_MEETING_ATTENDEE (MEETING_ID),
    INDEX IND_USER_ATTENDEE (USER_ID),
    FOREIGN KEY (MEETING_ID) REFERENCES MEETING(ID),
    FOREIGN KEY (USER_ID) REFERENCES USER(ID));
    """,
    """
    CREATE TABLE GOAL (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    MEETING_ID INT,
    GOAL_NAME VARCHAR(100) NOT NULL,
    INDEX IND_MEETING_GOAL (MEETING_ID),
    FOREIGN KEY (MEETING_ID) REFERENCES MEETING(ID));
    """,
    """
    CREATE TABLE VOTE (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    DECISION BOOLEAN DEFAULT NULL,
    GOAL_ID INT,
    USER_ID INT,
    INDEX IND_GOAL_VOTE (GOAL_ID),
    INDEX IND_USER_VOTE (USER_ID),
    FOREIGN KEY (GOAL_ID) REFERENCES GOAL(ID),
    FOREIGN KEY (USER_ID) REFERENCES USER(ID));
    """,
    """
    CREATE TABLE SKILL (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    MEETING_ID INT,
    SKILL_NAME VARCHAR(100) NOT NULL,
    INDEX IND_MEETING_SKILL (MEETING_ID),
    FOREIGN KEY (MEETING_ID) REFERENCES MEETING(ID));
    """,
    """
    CREATE TABLE RATING (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    RATING INT,
    SKILL_ID INT,
    RATING_FOR INT,
    RATING_BY INT,
    INDEX IND_SKILL_RATING (SKILL_ID),
    INDEX IND_FOR_RATING (RATING_FOR),
    INDEX IND_BY_RATING (RATING_BY),
    FOREIGN KEY (SKILL_ID) REFERENCES SKILL(ID),
    FOREIGN KEY (RATING_FOR) REFERENCES USER(ID),
    FOREIGN KEY (RATING_BY) REFERENCES USER(ID));
    """]

    for query in queryList:
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print("Query Executed")

    connection.close()
    print("MySQL connection is closed")


create_itoi_db(str(sys.argv[1]))