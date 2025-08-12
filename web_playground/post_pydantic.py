from typing import Optional

from pydantic import BaseModel, validator, field_validator


class post_pyd(BaseModel):

    userID: int
    id: int
    title: str
    body: str
    notes: Optional[str]= None



    @field_validator('id')
    @classmethod
    def validate_id(cls,v):
        if v == 0:
            return ValueError('id cannot be 0')
        return v

