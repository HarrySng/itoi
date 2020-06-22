from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

pswd = str(sys.argv[1])
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:{}@localhost:3306/ITOI_DB'.format(pswd),echo=True)
Base = automap_base()
Base.prepare(engine, reflect=True)

ORG = Base.classes.ORG
session = Session(engine)

session.query(ORG).first()