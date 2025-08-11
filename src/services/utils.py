import validate_docbr as docbr
import re

class Validator:
    @staticmethod
    def cpf(cpf: str) -> bool:
        cpf_validator = docbr.CPF()
        return cpf_validator.validate(cpf)
    
    @staticmethod
    def phone(phone: str) -> bool:
        regex = r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}-?[0-9]{4}$'
        return bool(re.match(regex, phone))
    
    @staticmethod
    def name(name: str) -> bool:
        regex = r'^([A-Za-zÀ-ú\s\'-]+( [A-Za-zÀ-ú\s\'-]+)*)$'
        return bool(re.match(regex, name))
    
    @staticmethod
    def value(value: float) -> bool:
        return isinstance(value, (int, float)) and value >= 0
    
    
class Cleaner:
    @staticmethod
    def clean_phone(phone: str) -> str:
        return re.sub(r'\D', '', phone)
    
    @staticmethod
    def clean_cpf(cpf: str) -> str:
        return re.sub(r'\D', '', cpf)
    
    @staticmethod
    def clean_name(name: str) -> str:
        return re.sub(r'[^\w\s]', '', name)
    
