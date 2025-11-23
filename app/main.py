from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.api.contacts import router as contacts_router

app = FastAPI(title="Contacts API")

app.include_router(auth_router)  # prefix вєе є в auth.py
app.include_router(contacts_router)  # prefix вже є в contacts.py

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Contacts API is running"}
