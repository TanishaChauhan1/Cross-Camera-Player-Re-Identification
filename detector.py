from ultralytics import YOLO
import cv2

class PlayerDetector:
    def __init__(self, model_path='best.pt'):
        self.model = YOLO(model_path)

    def detect_players(self, video_path):
        cap = cv2.VideoCapture(video_path)
        detections = []
        frame_id = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model.predict(frame, conf=0.4, verbose=False)[0]
            boxes = results.boxes.xyxy.cpu().numpy()
            classes = results.boxes.cls.cpu().numpy()

            players = [box for box, cls in zip(boxes, classes) if int(cls) == 0]  # Assuming class 0 is 'player'

            for box in players:
                x1, y1, x2, y2 = map(int, box)
                crop = frame[y1:y2, x1:x2]
                detections.append({'frame': frame_id, 'bbox': box, 'crop': crop})

            frame_id += 1

        cap.release()
        return detections
