from typing import List
import jwt

def encoding(user_info, token_key: str, 
             algorithm: str):
    encode_token = jwt.encode(user_info, token_key, algorithm)
    return {"token": encode_token}

def decoding(encode_token, token_key: str, 
             algorithm: str):
    user_info = jwt.decode(encode_token, token_key, algorithm)
    return {"data": user_info}