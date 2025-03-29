from pydantic import BaseModel,Field
from enum import Enum
from datetime import datetime

class ModelName(str,Enum):
    gemini_flash='gemini-1.5-flash'

class QueryInput(BaseModel):
    question:str
    session_id:str=Field(default=None)
    model:ModelName=Field(default=ModelName.gemini_flash)

class QueryResponse(BaseModel):
    answer:str
    session_id:str
    model:ModelName

class DocumentInfo(BaseModel):
    id:int
    filename:str
    upload_timestamp:datetime

class DeleteFileRequest(BaseModel):
    file_id:int

