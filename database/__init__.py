from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///database/library.db", echo=True, future=True)


from .book_db import *
from .customer_db import *
from .loan_db import *

