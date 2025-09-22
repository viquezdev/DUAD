import jwt


class JwtManager:
    def __init__(self, secret_key: str, algorithm: str = "HS256", expires_minutes: int = 15):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expires_minutes = expires_minutes

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.secret_key, algorithm=self.algorithm)
            return encoded
        except:
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None