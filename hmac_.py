import hmac
import hashlib
import secrets

def generate_challenge():
    return secrets.token_bytes(16)

def create_response(challenge, bit , secret_key_in):
    secret_key = secret_key_in.encode()
    message = challenge + bytes([bit])  
    return hmac.new(secret_key, message, hashlib.sha256).digest()

# Function to verify response
def verify_response(expected_response, received_response):
    # expected_response = create_response(challenge, bit , secret_key_in)
    return hmac.compare_digest(expected_response, received_response)


