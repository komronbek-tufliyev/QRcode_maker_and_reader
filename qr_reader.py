import cv2

d = cv2.QRCodeDetector()

val,  _,  _ = d.detectAndDecode(cv2.imread("youtube.png"))
print("Decoded text is: ", val)