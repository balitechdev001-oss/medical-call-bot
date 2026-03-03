from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AgeRequest(BaseModel):
    age: int

@app.post("/check-age")
def check_age(data: AgeRequest):
    try:
        age = int(data.age)

        if age >= 65:
            return {"message": "Aap medical services ke liye fit hain."}
        elif age > 0:
            return {"message": "Maaf kijiye. Aap eligible nahi hain."}
        else:
            return {"message": "Invalid age entered."}

    except:
        return {"message": "Age samajh nahi aayi."}