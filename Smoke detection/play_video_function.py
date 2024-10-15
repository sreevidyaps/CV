import cv2
def play_video(video_path):
    cap =cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: could not open video file")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break 
    cap.release()
    cv2.destroyAllWindows()
video_path = (r"C:\Users\AMZ PC\OneDrive\Desktop\CV\Smoke detection\3826855-hd_1920_1080_24fps.mp4")
play_video(video_path)


