import cv2

def annotate_video(video_path, detections, id_mapping, save_path, source='broadcast'):
    cap = cv2.VideoCapture(video_path)
    out = None
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        for i, det in enumerate(detections):
            if det['frame'] == frame_id:
                x1, y1, x2, y2 = map(int, det['bbox'])
                player_id = i if source == 'broadcast' else id_mapping.get(i, -1)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"ID: {player_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        if out is None:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(save_path, fourcc, 30, (frame.shape[1], frame.shape[0]))

        out.write(frame)
        frame_id += 1

    cap.release()
    out.release()
