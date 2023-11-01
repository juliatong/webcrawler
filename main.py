import re
import pyotp
import OTPGenerator 
from fastapi import FastAPI, HTTPException, status


app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Hello, World!"}



@app.post("/otp",  status_code=201)
def trigger_OTP(mobile_number: str = None, email_address:str= None, user_id: str = None):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
   
    if (not mobile_number.isdigit() or len(mobile_number) != 8) or(re.match(pattern, email_address) is None):
        raise HTTPException(status_code=400, detail="Invalid mobile number or email address")
       
    secret_key=retrieve_secret(mobile_number, email_address, user_id)
    otp_generator = OTPGenerator(secret_key)
    otp=otp_generator.generate_totp()
   
    #send_OTP(mobile_number, otp)
   
    return {
        "status": "success",
        "user_id": "",
        "mobile_number": "",
        "otp": "123456"
    }




@app.get("/otp", status_code=200)
def verify_totp(user_provided_otp: str, mobile_number: str= None, email_address: str = None, user_id: str = None):
    #validate
   
    secret_key=retrieve_secret(mobile_number, email_address, user_id)
    otp_generator = OTPGenerator(secret_key)
    expected_otp=otp_generator.generate_totp()
       
    # Compare the user-provided OTP with the expected OTP
    if expected_otp == user_provided_otp:
        return {
            "success": true,
            "message": "Authentication successful",
            "data": {
                "user_id": "12345",
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            }
        }
    else:
        raise HTTPException(status_code=401, detail="Authentication failed. Invalid OTP.The provided OTP is incorrect. Please try again.")


   
   
def retrieve_secret(mobile_number: str = None, email_address:str= None, user_id: str = None):
    return "my$3cr3tK3yF0rJWT$tr1ng"
