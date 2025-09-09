# usando pydantic com python 
# pip install pydantic 

from pydantic import BaseModel, field_validator

class User(BaseModel):
    nome: str
    idade: int
    email: str

    @field_validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('E-mail está inválido')
        return value


user1 = User(
    nome='Roberto',
    idade=21,
    email='robertodev04@gmail.com'
)

print(user1)



