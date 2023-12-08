from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Column

Base = declarative_base()

class Users(Base):
    __tablename__ = "userstable"
    id = Column(VARCHAR(8), primary_key=True)
    first_name = Column(VARCHAR(25))
    last_name = Column(VARCHAR(25))
    email = Column(VARCHAR(25))

    def __str__(self):
        return f"id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, email: {self.email}"