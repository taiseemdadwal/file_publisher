# SQLAlchemy models and enums for file publishing

import enum
import datetime
from sqlalchemy import Column, Integer, String, Boolean, Float, Enum, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PublishedSite(enum.Enum):
    van = "van"
    lon = "lon"

class FileRecord(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    on_disk = Column(Boolean, default=True)
    published_site = Column(Enum(PublishedSite), nullable=False)
    size_in_mb = Column(Float, nullable=False)
    is_infrastructure = Column(Boolean, default=False)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)
