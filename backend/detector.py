from ultralytics import YOLO
import cv2
import numpy as np

class CrowdDetector:
    def __init__(self, model_name='yolov8n.pt'):
        self.model = YOLO(model_name)
        # Thresholds for density levels
        self.LOW_THRESHOLD = 10
        self.MEDIUM_THRESHOLD = 25

    def detect_and_count(self, image):
        """
        Detects people in the image and returns the count, density level, and annotated image.
        """
        results = self.model(image, classes=[0]) # class 0 is person
        
        count = 0
        annotated_frame = image.copy()

        for result in results:
            boxes = result.boxes
            count = len(boxes)
            annotated_frame = result.plot()

        density_level = self._get_density_level(count)
        
        return {
            "count": count,
            "density_level": density_level,
            "annotated_frame": annotated_frame
        }

    def _get_density_level(self, count):
        if count < self.LOW_THRESHOLD:
            return "Low"
        elif count < self.MEDIUM_THRESHOLD:
            return "Medium"
        else:
            return "High"
