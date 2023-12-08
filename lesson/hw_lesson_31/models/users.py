from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Column

Base = declarative_base()

class Users(Base):
    __tablename__ = "lesson_30"
    id = Column(VARCHAR(255), primary_key=True)
    name = Column(VARCHAR(255))
    createdAt = Column(VARCHAR(255))

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, createdAt: {self.createdAt}"