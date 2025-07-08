🏀 Cross-Camera Player Re-Identification

This project solves a player re-identification challenge using two videos captured from different camera angles. It ensures players maintain consistent IDs across the two feeds.

📁 Folder Structure

.
├── best.pt                # YOLOv11 model (trained to detect players)
├── broadcast.mp4          # Broadcast camera video
├── tacticam.mp4           # Tacticam camera video
├── main.py                # Main script to run the full pipeline
├── detector.py            # Player detection logic
├── matcher.py             # Feature extraction and matching
├── utils.py               # Visualization and video output
├── requirements.txt       # Dependencies

🧪 Setup Instructions

Install dependencies:

pip install -r requirements.txt

Place files:

Put broadcast.mp4, tacticam.mp4, and best.pt in the root folder.

Run the program:

python main.py

This will generate two new files:

broadcast_annotated.mp4

tacticam_annotated.mp4

🛠️ Components

main.py

Orchestrates detection, feature extraction, matching, and annotation.

detector.py

Detects players using YOLOv11.

matcher.py

Extracts HSV histograms from player crops.

Matches players using cosine similarity.

utils.py

Annotates videos with bounding boxes and player IDs.

📦 Dependencies

ultralytics
opencv-python
numpy
scipy

🧠 Notes

Class 0 is assumed to be the player class in YOLO.

Appearance feature is based on HSV histogram.

Matching is based purely on visual similarity (not spatial/temporal for now).

📩 Output

You will find annotated videos with consistent player IDs saved in the project folder after successful execution.

📬 Contact

For help or feedback, feel free to reach out!

