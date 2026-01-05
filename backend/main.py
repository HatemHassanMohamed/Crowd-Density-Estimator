from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import io
from detector import CrowdDetector

app = FastAPI(title="Crowd Density Estimator")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

detector = CrowdDetector()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze-frame")
async def analyze_frame(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file")

        result = detector.detect_and_count(image)
        
        # Encode annotated image to base64 or return as separate stream? 
        # For simplicity, let's return JSON with metadata and maybe we can add an endpoint for the image later
        # or just return the raw data.
        
        return {
            "count": result["count"],
            "density_level": result["density_level"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-frame-image")
async def analyze_frame_image(file: UploadFile = File(...)):
    """
    Returns the annotated image directly.
    """
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file")

        result = detector.detect_and_count(image)
        annotated_frame = result["annotated_frame"]
        
        _, encoded_img = cv2.imencode('.jpg', annotated_frame)
        return StreamingResponse(io.BytesIO(encoded_img.tobytes()), media_type="image/jpeg")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
