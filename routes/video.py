from fastapi import APIRouter, Query, Depends, HTTPException
from typing import Optional
import boto3
from botocore.exceptions import ClientError
from sqlalchemy.orm import Session
from models.user import User
from models.video import Video
from middleware.auth import get_current_user
from config.database import get_db
from models.permission import VideoPermission

router = APIRouter()
s3_client = boto3.client('s3')

@router.get("/")
async def get_video(
    folder: Optional[str] = Query(None, description="Folder path in S3"),
    filename: str = Query(..., description="Name of the video file"),
    bucket: Optional[str] = Query(None, default="your-bucket-name")
):
    try:
        # Construct the full path
        key = f"{folder}/{filename}" if folder else filename
        
        # Generate a presigned URL for the video
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket,
                'Key': key
            },
            ExpiresIn=3600  # URL expires in 1 hour
        )
        
        return {
            "status": "success",
            "url": presigned_url,
            "filename": filename,
            "folder": folder
        }
        
    except ClientError as e:
        return {
            "status": "error",
            "message": str(e)
        }

@router.get("/{video_id}")
async def get_video(
    video_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
        
    # Check if user has access to the video
    has_permission = (
        video.owner_id == current_user.id or
        db.query(VideoPermission)
        .filter(
            VideoPermission.video_id == video_id,
            VideoPermission.user_id == current_user.id
        ).first() is not None
    )
    
    if not has_permission:
        raise HTTPException(status_code=403, detail="Access denied")
        
    return video