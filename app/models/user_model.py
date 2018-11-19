import datetime
import jwt
from app import app, conn,bcrypt

cur = conn.cursor()

class User:
    """
    Table schema
    """

    cur.execute('''CREATE TABLE IF NOT EXISTS users
            ( user_id SERIAL PRIMARY KEY    NOT NULL,
            email             VARCHAR(255)     NOT NULL,
            password          VARCHAR(255)     NOT NULL,
            registered_on     DATE     NOT NULL );''')

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')) \
            .decode('utf-8')
        self.registered_on = str(datetime.datetime.now())

    def save(self):
        """
        Persist the user in the database
        :param user:
        :return:
        """
        cur = conn.cursor()
        sql = """
            INSERT INTO Users (email,password,registered_on) 
                    VALUES (%s,%s,%s)
        """
        cur.execute(sql,(self.email,self.password,self.registered_on,))
        conn.commit()

    @staticmethod
    def get_by_email(user_email):
        """
        Filter a user by email.
        :param user_id:
        :return: User or None
        """
        cur = conn.cursor()
        sql1 = """
             SELECT * FROM Users WHERE email=%s
        """
        cur.execute(sql1,(user_email,))
        user = cur.fetchone()
        return user

    @staticmethod
    def encode_auth_token(user_id):
        """
        Encode the Auth token
        :param user_id: User's Id
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days = 1),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token):
        """
        Decoding the token to get the payload and then return the user Id in 'sub'
        :param token: Auth Token
        :return:
        """
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'],algorithms='HS256')
            is_token_blacklisted = BlackListToken.check_blacklist(token)
            if is_token_blacklisted:
                return 'Token was Blacklisted, Please login In'
            return payload['sub']
        except jwt.ExpiredSignatureError:
             return 'Signature expired, Please sign in again'
        except jwt.InvalidTokenError:
             return 'Invalid key. Please sign in again'