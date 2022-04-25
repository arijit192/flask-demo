import jwt

SECRET = "thisissecretforjwt"

def verify_token(token):
    try:
        jwt.decode(token,SECRET,["HS256"])
        return True
    except:
        return False

    
def create_token(payload):
    return jwt.encode(payload,SECRET)

def get_data(token):
    return jwt.decode(token,SECRET,["HS256"])

def extract_token(twb):
    return twb[7:]