import cv2

cap=cv2.VideoCapture('test.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
delay=int((1/fps)*1000)
while True:
    success,frame=cap.read()
    if True==success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",gray)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

