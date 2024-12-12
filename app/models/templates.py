import re

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Dict, Any

from app.database.db import db


class FieldType(Enum):
    email = 'email'
    phone = 'phone'
    data = 'data'
    text = 'text'


class Template(BaseModel):
    name: str
    fields: Dict[str, FieldType]


class IncomingTemplate(BaseModel):
    fields: Dict[str, Any]

    class Config:
        str_min_length = 1
        str_strip_whitespace = True

    @staticmethod
    def phone_valid(value: str) -> bool:
        regex_phone = r'\+7 \d{3} \d{3} \d{2} \d{2}'
        return bool(re.match(regex_phone, value))

    @staticmethod
    def date_valid(value: str) -> bool:
        for date_format in ['%d.%m.%Y', '%Y-%m-%d']:
            try:
                datetime.strptime(value, date_format)
            except ValueError:
                continue
        return False

    @staticmethod
    def email_valid(value: str) -> bool:
        try:
            EmailStr.validate(value)
            return True
        except ValidationError:
            return False

    def detect_field_type(self, value: str) -> str:
        if self.date_valid(value):
            return FieldType.date
        if self.phone_valid(value):
            return FieldType.phone
        if self.email_valid(value):
            return FieldType.email
        return FieldType.text

    def find_matching_tempalte(self) -> str:
        for template in db.all():
            is_matching = True
            for field_name, field_type in template['fields'].items():
                if field_name not in self.fields:
                    is_matching = False
                    break

                value = self.fileds[field_name]
                detected_type = self.detect_field_type(value)
                if detected_type != field_type:
                    is_matching = False
                    break
            if is_matching:
                return template['name']

        return {field_name: self.detect_field_type(value) for field_name,
                value in self.fields.items()}
