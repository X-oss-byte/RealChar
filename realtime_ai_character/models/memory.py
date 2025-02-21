from sqlalchemy import Column, Integer, String
from realtime_ai_character.database.base import Base
from pydantic import BaseModel
from typing import Optional


class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    quivr_api_key = Column(String)
    quivr_brain_id = Column(String)

    def save(self, db):
        db.add(self)
        db.commit()

class UpdateMemoryRequest(BaseModel):
    quivr_api_key: Optional[str] = None
    quivr_brain_id: Optional[str] = None