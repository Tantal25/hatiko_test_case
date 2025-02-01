from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class IMEISchema(BaseModel):
    imei: str = Field(min_length=15, max_length=15)
    token: str

    model_config = ConfigDict(
        str_strip_whitespace=True
    )


class UserSchema(BaseModel):
    username: str
    telegram_id: Optional[int] = None

    model_config = ConfigDict(
        str_strip_whitespace=True
    )
