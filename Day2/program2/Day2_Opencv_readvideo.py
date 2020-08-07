import cv2

cap=cv2.VideoCapture('test.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
delay=int((1/fps)*1000)
while True:
    success,frame=cap.read()
    if True==success:
        cv2.imshow("frame",frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

