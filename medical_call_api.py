from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

@app.post("/voice")
async def voice(request: Request):
    form = await request.form()
    age = form.get("SpeechResult")

    response = VoiceResponse()

    # Agar pehli baar call hua (age nahi mili)
    if not age:
        gather = response.gather(
            input="speech",
            action="/voice",
            method="POST"
        )
        gather.say("Assalam o Alaikum. Medical screening ke liye apni age batayein.")
        return Response(str(response), media_type="application/xml")

    # Age extract karein
    try:
        age_number = int(''.join(filter(str.isdigit, age)))

        if age_number >= 65:
            response.say("Aap medical services ke liye eligible hain. Shukriya.")
        else:
            response.say("Maazrat. Medical services sirf 65 saal ya us se zyada age ke liye hain.")

    except:
        response.say("Age samajh nahi aayi. Dobara call karein.")

    response.hangup()

    return Response(str(response), media_type="application/xml")