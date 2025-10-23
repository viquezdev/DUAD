import jwt
from pathlib import Path


class JwtManager:
    def __init__(self, private_key, public_key, algorithm="RS256"):
        self.private_key = private_key
        self.public_key=public_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            token = jwt.encode(data, self.private_key, algorithm=self.algorithm)
            print("Generated Token:", token)
            return token
        except Exception as e:
            print(e)
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            print("Decoded Payload:", decoded)
            return decoded
        except Exception as e:
            print(e)
            return None
        
base_path = Path(__file__).resolve().parent.parent
with open(base_path / "keys" / "private.pem", "rb") as f:
    private_key = f.read()

with open(base_path / "keys" / "public.pem", "rb") as f:
    public_key = f.read()

jwt_manager=JwtManager(private_key=private_key,public_key=public_key)