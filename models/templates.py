from datetime import datetime
import re

from pydantic import BaseModel, EmailStr
from typing import Dict, Any


class FieldType(str):
    email = 'email'
    phone = 'phone'
    data = 'data'
    text = 'text'


class Template(BaseModel):
    name: str
    fields: Dict[str, FieldType]


class IncomingTemplate(BaseModel):
    fileds: Dict[str, Any]

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True

    @staticmethod
    def phone_valid(value: str) -> bool:
        regex_phone = r'\+7 \d{3} \d{3} \d{2} \d{2}'
        return bool(re.match(regex_phone, value))
    
    @staticmethod
    def date_valid(value: str) ->bool:
        for date_format in ['%d.%m.%Y', '%Y-%m-%d']:
            try:
                datetime.strptime(value, date_format)
            except ValueError:
                continue
        return  False


    @staticmethod
    def email_valid(value: str) ->bool:
        try:
            EmailStr.validate(value)
            return True
        except ValueError:
            return False
