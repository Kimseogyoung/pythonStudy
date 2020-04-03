#카메라　캡처　코드

import cv2


def capturecam():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)  # 좌우 반전
        cv2.imshow('image', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('a.jpg', frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
            break
    cv2.destroyAllWindows()
