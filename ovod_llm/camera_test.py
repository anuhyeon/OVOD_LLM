import cv2

cap = cv2.VideoCapture(0)  # 웹캠 디바이스 ID (0번 디바이스)
print("Default FPS:", cap.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()