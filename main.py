import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect_people(image_path: str):
    img = cv2.imread(image_path)
    img = imutils.resize(img,
                         width=min(400, img.shape[1]))

    (frame, _) = hog.detectMultiScale(img,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.05)

    number_of_people = 0
    for x, y, w, h in frame:
        cv2.rectangle(img,
                      (x, y),
                      (x + w, y + h),
                      (0, 255, 0),
                      2)
        number_of_people += 1
    cv2.putText(img,
                f'{number_of_people} person detected',
                (20, 30),
                cv2.FONT_HERSHEY_DUPLEX,
                1,
                (255, 0, 0),
                2)

    cv2.imshow("Person detector", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect_people("photos/photo1.jpg")
    detect_people("photos/photo2.jpg")
    detect_people("photos/photo3.jpg")
    detect_people("photos/photo4.jpg")
