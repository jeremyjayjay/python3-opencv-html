import cv2

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frameq
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # 指定保存的路径和文件名
        cv2.imwrite("C:/Users/Administrator/Desktop/pic/face/te1.jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()