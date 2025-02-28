from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, video
from config.database import engine
from models import user, video

# Create database tables
user.Base.metadata.create_all(bind=engine)
video.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(video.router, prefix="/api/videos", tags=["videos"]) 