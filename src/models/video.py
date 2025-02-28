from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.database import Base
import uuid

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # Add any other fields you need
    
    owner = relationship("User", back_populates="videos")

    def __repr__(self):
        return f"<Video(id={self.id}, title={self.title})>" 