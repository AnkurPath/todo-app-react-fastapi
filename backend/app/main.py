from fastapi import FastAPI ,Depends
from core.database import Database
from core import models
from core.database import Database
from api.router import router1
from middleware.authentication import UserAuthorizationMiddleware
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=Database().db_engine())


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allows these HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the authorization middleware
authorization_middleware = UserAuthorizationMiddleware()

# Include router1 with the /api prefix
app.include_router(router1, prefix="/api", dependencies=[Depends(authorization_middleware)])

