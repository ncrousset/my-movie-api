import main
from fastapi.encoders import jsonable_encoder
from jwt import encode, decode

algorithm = 'HS256'

def create_token(data: dict):
    data = jsonable_encoder(data)
    token: str = encode(payload=data, key=main.KEY_SECRET, algorithm=algorithm)
    return token

def validate_token(token: str)-> dict:
    try:
        decoded_token: dict = decode(token, key=main.KEY_SECRET, algorithms=algorithm) 
        return decoded_token
    except:
        return None