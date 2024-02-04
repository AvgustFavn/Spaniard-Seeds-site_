from datetime import datetime
from pathlib import Path

from sqlalchemy import *
from sqlalchemy import event
from sqlalchemy.orm import Session, declarative_base, relationship

engine = create_engine("postgresql+psycopg2://test:Some_password@localhost/test_basee")
session = Session(bind=engine)
BASE_DIR = Path(__file__).resolve().parent

Base = declarative_base()

class User_tg(Base):
    __tablename__ = 'user_bot_tg'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(Text, nullable=False)

Base.metadata.create_all(engine)
