from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:Addidass1988@localhost:5432/postgres")

__session = sessionmaker(bind=engine)
session = __session()