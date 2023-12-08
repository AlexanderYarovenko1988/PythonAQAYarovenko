from sqlalchemy import Column, VARCHAR, create_engine, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Lesson30(Base):
    __tablename__ = 'lesson_30'
    id = Column(VARCHAR(255), primary_key=True)
    name = Column(VARCHAR(255))
    createdAt = Column(DateTime, default=datetime.utcnow)

# Создаем подключение к базе данных
DATABASE_URL = "postgresql://postgres:Addidass1988@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

# Создаем таблицу в базе данных
Base.metadata.create_all(bind=engine)

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()
