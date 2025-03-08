from fastapi import FastAPI
from database import create_database
from fastapi.middleware.cors import CORSMiddleware
from autentication.auth_endpoints import auth_router
from users.users_endpoint import users_router
from testgroups.testsgrops_endpoints import testgroup_router 

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
app = FastAPI(
    openapi_tags=[
        {
            "name": "Authentication",
            "description": "Endpoints for user authentication and OTP management.",
        },
        {
            "name": "Users",
            "description": "Endpoints for user profile management.",
        }
    ]
)

"""
@app.on_event("startup")
def on_startup():
    create_database()
# TODO : CHANGE WITH ALEMBIC
# """

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(testgroup_router)