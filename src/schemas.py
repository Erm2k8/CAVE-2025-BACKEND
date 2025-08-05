from pydantic import BaseModel, field_validator
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