from typing import Optional
from pydantic import BaseModel, field_validator
from enum import Enum
from services.utils import Validator

class BidCreate(BaseModel):
    amount: float
    cpf: str
    phone: str
    name: str

    @field_validator('amount')
    def validate_amount(cls, value):
        if not Validator.value(value):
            raise ValueError("Valor do lance inválido")
        return value

    @field_validator('cpf')
    def validate_cpf(cls, value):
        if not Validator.cpf(value):
            raise ValueError("CPF inválido")
        return value

    @field_validator('phone')
    def validate_phone(cls, value):
        if not Validator.phone(value):
            raise ValueError("Telefone inválido")
        return value
    
    @field_validator('name')
    def validate_name(cls, value):
        if not Validator.name(value):
            raise ValueError("Nome inválido")
        return value
    

class Format(str, Enum):
    excel = "excel"
    csv = "csv"
    json = "json"

class ReportCreate(BaseModel):
    format: Format

    @field_validator('format')
    def validate_format(cls, value):
        if value not in [Format.csv, Format.excel, Format.json]:
            raise ValueError("Formato inválido. Use 'csv', 'excel' ou 'json'.")
        return value
    

class UserLogin(BaseModel):
    username: str
    password: str