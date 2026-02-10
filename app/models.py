from pydantic import BaseModel
from datetime import datetime
import uuid

device = {}

class DeviceCreate(BaseModel):
    hostname: str
    ip_address: str

class Device(DeviceCreate):
    id: str
    created_at: datetime