from fastapi import FastAPI 
from app.routers import movie as movies_router, auth as auth_router, user as user_router
from config.database import engine, Base
from app.middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router.router)
app.include_router(movies_router.router)
app.include_router(user_router.router)

# For debugging with breakpoints 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)