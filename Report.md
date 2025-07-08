<h1>📑 Player Re-Identification: Cross-Camera Mapping Report </h1>

<h2>🎯 Objective</h2>
To ensure consistent player IDs across two different video feeds (`broadcast.mp4` and `tacticam.mp4`) of the same match using computer vision techniques.

---

<h2>🧭 Methodology</h2> 

### 1. **Player Detection**
- We used a fine-tuned YOLOv11 model (`best.pt`) to detect players.
- Each frame was processed to extract bounding boxes for players (assumed class 0).

### 2. **Feature Extraction**
- For each detected player crop, HSV color histograms were computed.
- Histograms were normalized and flattened into feature vectors.

### 3. **Cross-View Matching**
- Cosine similarity was used to match players from `broadcast` to `tacticam`.
- The player in `tacticam` with the most visually similar histogram (smallest cosine distance) was matched to the broadcast player.

### 4. **Annotation and Output**
- Videos were reprocessed to overlay bounding boxes and assigned player IDs.
- Two annotated videos were generated:
  - `broadcast_annotated.mp4`
  - `tacticam_annotated.mp4`

---

## 🔬 Techniques Tried

- **Appearance-based matching**:
  - HSV histogram was effective for initial prototype.
  - Simple and computationally efficient.

- **Alternative Considered (not implemented)**:
  - Deep features (e.g., embeddings from a re-ID model like OSNet)
  - Temporal consistency (track player movement over time)
  - Spatial alignment using homography

---

## 🧱 Challenges Faced

- **Occlusion and motion blur** in both videos
- Players having similar uniforms
- No player jersey number OCR for confirmation

---

## ✅ What Works

- End-to-end reproducible pipeline.
- IDs are reasonably consistent when players differ in appearance.
- Output is clear and interpretable.

---

## ❌ Limitations

- Players with similar appearance may be confused.
- No temporal tracking or motion modeling.

---

## 🧩 Future Work

- Integrate Deep Re-ID networks (OSNet, FastReID).
- Add temporal tracking (e.g., DeepSORT or ByteTrack).
- Use pose estimation or team formations for matching.
- Include player jersey number detection for validation.

---

## 📦 Project Status

**Complete prototype.** All core functionality works. With more time, we would:
- Improve matching robustness.
- Add real-time re-identification support.
- Run benchmark evaluations.

---

