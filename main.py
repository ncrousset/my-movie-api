from fastapi import FastAPI 
from app.routers import movie as movies_router, \
                auth as auth_router, user as user_router
from config.database import engine, Base
from app.middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

KEY_SECRET = "SECRET"

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost"
]

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router.router)
app.include_router(movies_router.router)
app.include_router(user_router.router)

# For debugging with breakpoints 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)