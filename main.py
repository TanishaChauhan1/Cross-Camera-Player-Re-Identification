from detector import PlayerDetector
from matcher import compute_features, match_players
from utils import annotate_video

# Step 1: Detect players
print("Detecting players in broadcast.mp4...")
detector = PlayerDetector()
det_broadcast = detector.detect_players("broadcast.mp4")

print("Detecting players in tacticam.mp4...")
det_tacticam = detector.detect_players("tacticam.mp4")

# Step 2: Extract features
print("Extracting features...")
features_broadcast = compute_features(det_broadcast)
features_tacticam = compute_features(det_tacticam)

# Step 3: Match players
print("Matching players across cameras...")
mapping = match_players(features_broadcast, features_tacticam)
print("Player mapping:", mapping)

# Step 4: Annotate and save videos
print("Annotating broadcast video...")
annotate_video("broadcast.mp4", det_broadcast, {}, "broadcast_annotated.mp4", source='broadcast')

print("Annotating tacticam video with mapped IDs...")
annotate_video("tacticam.mp4", det_tacticam, {v: k for k, v in mapping.items()}, "tacticam_annotated.mp4", source='tacticam')

print("Done! Annotated videos saved.")
