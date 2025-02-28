from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.database import Base
import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    videos = relationship("Video", back_populates="owner")

    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str):
        return pwd_context.verify(plain_password, self.password) 