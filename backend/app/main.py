from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.operations import operations_router
from app.settings import Settings

# Fast API config
app = FastAPI(
    title="BragApp",
    description="It's full of things but ... hey, it's just a showoff 🤷🏻‍♂️",
    version="0.0.1989",
    contact={
        "name": ":#/ Gioele SL Fierro",
        "url": "https://gslf.it/",
        "email": "hck@gslf.it",
    },
)

# CORS Config
settings = Settings()
origins = [
    settings.FRONTEND_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# Include the router from the operations endpoint
app.include_router(operations_router)