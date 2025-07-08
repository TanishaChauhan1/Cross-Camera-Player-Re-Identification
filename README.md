<h1>🏀 Cross-Camera Player Re-Identification</h1>

This project solves a player re-identification challenge using two videos captured from different camera angles. It ensures players maintain consistent IDs across the two feeds.

<h2>📁 Folder Structure</h2>

<h1>Since the best.pt file is too big to upload here's the link: https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view</h1>
.
├── best.pt                # YOLOv11 model (trained to detect players)
├── broadcast.mp4          # Broadcast camera video
├── tacticam.mp4           # Tacticam camera video
├── main.py                # Main script to run the full pipeline
├── detector.py            # Player detection logic
├── matcher.py             # Feature extraction and matching
├── utils.py               # Visualization and video output
├── requirements.txt       # Dependencies

<h2>🧪 Setup Instructions</h2>

Install dependencies:

pip install -r requirements.txt

Place files:

Put broadcast.mp4, tacticam.mp4, and best.pt in the root folder.

Run the program:

python main.py

This will generate two new files:

broadcast_annotated.mp4

tacticam_annotated.mp4

<h2>🛠️ Components</h2>

main.py

Orchestrates detection, feature extraction, matching, and annotation.

detector.py

Detects players using YOLOv11.

matcher.py

Extracts HSV histograms from player crops.

Matches players using cosine similarity.

utils.py

Annotates videos with bounding boxes and player IDs.

<h2>📦 Dependencies</h2>

ultralytics
opencv-python
numpy
scipy

<h2>🧠 Notes</h2>

Class 0 is assumed to be the player class in YOLO.

Appearance feature is based on HSV histogram.

Matching is based purely on visual similarity (not spatial/temporal for now).

<h1>📩 Output</h1>

You will find annotated videos with consistent player IDs saved in the project folder after successful execution.

<h2>📬 Contact</h2>

For help or feedback, feel free to reach out!

