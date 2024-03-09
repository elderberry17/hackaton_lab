import uvicorn
from fastapi import FastAPI, Depends

from connection import *
from models import *

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/participants/")
def register_participant(participant: ParticipantDefault, session=Depends(get_session)):
    participant = Participant.model_validate(participant)
    session.add(participant)
    session.commit()
    session.refresh(participant)

    return {"message": "Participant registered successfully"}


# Run the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
