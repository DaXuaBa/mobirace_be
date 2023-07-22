from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean,DateTime,Float,Double
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Table

class User(Base):
    __tablename__ = 'USER'
    USER_ID: Mapped[int] = mapped_column(primary_key=True)
    USER_NAME: Mapped[str] = mapped_column(String(50))
    PASSWORD: Mapped[str] = mapped_column(String(50))
    CREATED_AT: Mapped[DateTime] = mapped_column(DateTime)
    FULL_NAME: Mapped[str] = mapped_column(String(100))
    AVATAR_PATH: Mapped[str] = mapped_column(String(100))
    DATE_OF_BIRTH: Mapped[DateTime] = mapped_column(DateTime)
    GENDER: Mapped[str] = mapped_column(String(50))
    TEL_NUM: Mapped[str] = mapped_column(String(10))
    TOTAL_DISTANCE: Mapped[Double] = mapped_column(Double)
    RANKING: Mapped[int] = mapped_column(Integer)
    STATUS: Mapped[str] = mapped_column(String(50))
    LINK_FB: Mapped[str] = mapped_column(String(50))
    HOME_NUMBER: Mapped[str] = mapped_column(String(50))
    PRECINCT_ID: Mapped[str] = mapped_column(String(50))
    SIZE_ID: Mapped[int] = mapped_column(Integer)
    ORG_ID: Mapped[str] = mapped_column(String(50))
    ADDRESSES: Mapped[list["Address"]] = relationship(primaryjoin='foreign(ADDRESS.PRECINCT_ID) == PRECINCT_ID')
    POSTS: Mapped[list["Post"]] = relationship(primaryjoin='foreign(POST.USER_ID) == USER_ID')
    SHIRT_SIZE: Mapped[list["Shirt_Size"]] = relationship(primaryjoin='foreign(SHIRT_SIZE.SIZE_ID) == SIZE_ID')
    ORGS: Mapped[list["Organzation"]] = relationship(primaryjoin='foreign(ORGANZATION.ORGANZATION_ID) == ORGANZATION_ID')

class Role(Base):
    __tablename__='ROLE'
    ROLE_ID: Mapped[int] = mapped_column(primary_key=True)
    ROLE_NAME: Mapped[str] = mapped_column(String(50))
    STATUS: Mapped[str] = mapped_column(String(50))
    USER_ID: Mapped[int] = mapped_column(Integer)
    CREATED_AT: Mapped[DateTime] = mapped_column(DateTime)

UserRole = Table(
    "USER_ROLE",
    Base.metadata,
    Column("USER_ID", Integer, primary_key=True),
    Column("ROLE_ID", Integer, primary_key=True)
) 

class Function(Base):
    __tablename__='FUNCTION'
    FUNC_ID: Mapped[int] = mapped_column(primary_key=True)
    FUNC_NAME: Mapped[str] = mapped_column(String(50))
    STATUS: Mapped[str] = mapped_column(String(50))
    FUNC_PARENT_ID: Mapped[int] = mapped_column(Integer)
    API_PATH: Mapped[str] = mapped_column(String(100))
    USER_ID: Mapped[int] = mapped_column(Integer) 
    CREATED_AT: Mapped[DateTime] = mapped_column(DateTime)

RoleFunction = Table(
    "ROLE_FUNCTION",
    Base.metadata,
    Column("FUNC_ID", Integer, primary_key=True),
    Column("ROLE_ID", Integer, primary_key=True)
)

class Run(Base):
    __tablename__='RUN'
    RUN_ID: Mapped[int] = mapped_column(primary_key=True)
    USER_ID: Mapped[int] = mapped_column(Integer)
    STRAVA_ID: Mapped[int] = mapped_column(Integer)
    NAME: Mapped[str] = mapped_column(String(50))
    DISTANCE: Mapped[float] = mapped_column(Float)
    DURATION: Mapped[float] = mapped_column(Float)  
    PACE: Mapped[float] = mapped_column(Float)
    CALORI: Mapped[float] = mapped_column(Float)
    CREATED_AT: Mapped[DateTime] = mapped_column(DateTime)
    STATUS: Mapped[str] = mapped_column(String(50))
    TYPE: Mapped[str] = mapped_column(String(50)) 
    HEART_RATE: Mapped[Double] = mapped_column(Double)
    STEP_RATE: Mapped[Double] = mapped_column(Double)
    RUNS: Mapped[list["Run"]] = relationship(primaryjoin='foreign(RUN.USER_ID) == USER_ID')

class Club(Base):
    __tablename__='CLUB'
    CLUB_ID: Mapped[int] = mapped_column(primary_key=True)
    CLUB_NAME: Mapped[str] = mapped_column(String(100))
    DESCRIPTION: Mapped[str] = mapped_column(String(200))
    CREATE_AT: Mapped[DateTime] = mapped_column(DateTime)
    CLUB_TOTAL_DISTANCE: Mapped[Double] = mapped_column(Double)
    CLUB_RANKING: Mapped[int] = mapped_column(Integer)
    STATUS: Mapped[int] = mapped_column(Integer)
    USER_ID: Mapped[int] = mapped_column(Integer)
    ADMIN: Mapped[int] = mapped_column(Integer)
    MIN_PACE: Mapped[Double] = mapped_column(Double)
    MAX_PACE: Mapped[Double] = mapped_column(Double)
    PICTUTE_PATH: Mapped[str] = mapped_column(String(100))

UserRole = Table(
    "USER_CLUB",
    Base.metadata,
    Column("USER_ID", Integer, primary_key=True),
    Column("CLUB_ID", Integer, primary_key=True),
    Column("JOIN_DATE", DateTime),
    Column("TOTAL_DISTANCE", Double),
    Column("RANKING", Integer),
    Column("PACE", Double)
)

ClubEvent = Table(
    "CLUB_EVENT",
    Base.metadata,
    Column("CLUB_ID", Integer, primary_key=True),
    Column("EVENT_ID", Integer, primary_key=True),
    Column("JOIN_DATE", DateTime),
    Column("TOTAL_DISTANCE", Double),
    Column("RANKING", Integer),
    Column("PACE", Double)
)

class Event(Base):
    __tablename__='EVENT'
    EVENT_ID: Mapped[int] = mapped_column(primary_key=True)
    USER_ID: Mapped[int] = mapped_column(Integer)
    DESCRIPTION: Mapped[str] = mapped_column(String(100))
    TITLE: Mapped[str] = mapped_column(String(100))
    CREATE_AT: Mapped[DateTime] = mapped_column(DateTime)
    PICTURE_PATH: Mapped[str] = mapped_column(String(100))
    START_DATE: Mapped[DateTime] = mapped_column(DateTime)
    END_DATE: Mapped[DateTime] = mapped_column(DateTime)
    STATUS: Mapped[str] = mapped_column(String(100))
    RUNNING_CATEGORY: Mapped[str] = mapped_column(String(100))
    NUM_OF_ATTENDEE: Mapped[int] = mapped_column(Integer)
    NUM_OF_RUNNER: Mapped[int] = mapped_column(Integer)
    TOTAL_DISTANCE: Mapped[Double] = mapped_column(Double) 
    CONTENT: Mapped[LONGTEXT] = mapped_column(LONGTEXT)
    MIN_PACE: Mapped[Double] = mapped_column(Double)
    MAX_PACE: Mapped[Double] = mapped_column(Double)

UserEvent = Table(
    "USER_EVENT",
    Base.metadata,
    Column("USER_ID", Integer, primary_key=True),
    Column("EVENT_ID", Integer, primary_key=True),
    Column("JOIN_DATE", DateTime),
    Column("TOTAL_DISTANCE", Double),
    Column("RANKING", Integer),
    Column("PACE", Double)
)

class Post(Base):
    __tablename__='POST'
    POST_ID: Mapped[int] = mapped_column(primary_key=True)
    TITLE: Mapped[str] = mapped_column(String(100))
    USER_ID: Mapped[int] = mapped_column(Integer)
    CREATED_AT: Mapped[DateTime] = mapped_column(DateTime)
    HTML_CONTENT: Mapped[LONGTEXT] = mapped_column(LONGTEXT)

class Organzation(Base):
    __tablename__='ORGANZATION'
    ORG_ID: Mapped[str] = mapped_column(String(50),primary_key=True)
    ORG_NAME: Mapped[str] = mapped_column(String(100))
    ORG_PARENT_ID: Mapped[str] = mapped_column(String(50))
    ORGS: Mapped[list["Organzation"]] = relationship(primaryjoin='ORGANZATION.ORG_ID == ORG_PARENT_ID')

class Shirt_Size(Base):
    __tablename__='SHIRT_SIZE'
    SIZE_ID: Mapped[int] = mapped_column(primary_key=True)
    SIZE_NAME: Mapped[str] = mapped_column(String(100))

class Address(Base):
    __tablename__='ADDRESS'
    PROVINCE_ID: Mapped[str] = mapped_column(String(50), primary_key=True)
    DISTRICT_ID: Mapped[str] = mapped_column(String(100), primary_key=True)
    PRECINCT_ID: Mapped[str] = mapped_column(String(100), primary_key=True)
    NAME: Mapped[str] = mapped_column(String(100))
    FULL_NAME: Mapped[str] = mapped_column(String(100))
    STATUS: Mapped[str] = mapped_column(String(10))