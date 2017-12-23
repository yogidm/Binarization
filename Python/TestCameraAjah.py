import cv2
import numpy as np

def nothing(x):    
    pass

cv2.namedWindow('Setting Camera')

cv2.createTrackbar('Bri','Setting Camera',50,100,nothing)
cv2.createTrackbar('Con','Setting Camera',50,100,nothing)
cv2.createTrackbar('Sat','Setting Camera',50,100,nothing)
cv2.createTrackbar('Hue','Setting Camera',50,100,nothing)
cv2.createTrackbar('Gain','Setting Camera',50,100,nothing)
cv2.createTrackbar('Expo','Setting Camera',50,100,nothing)

cap = cv2.VideoCapture(1)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT
cap.set(10,0.5 ) #Brightness 0-1
cap.set(11,0.5 ) #Contrass 0-1
cap.set(12,0.5) #saturation 0-1
print cap.get(0)
print cap.get(1)
print cap.get(2)
print cap.get(3)
print cap.get(4)
print cap.get(5)
print cap.get(6)
print cap.get(7)
print cap.get(11)
print cap.get(12)
print cap.get(10)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    sBri = float(cv2.getTrackbarPos('Bri', 'Setting Camera'))
    sCon = float(cv2.getTrackbarPos('Con', 'Setting Camera'))
    sSat = float(cv2.getTrackbarPos('Sat', 'Setting Camera'))
    sHue = float(cv2.getTrackbarPos('Hue', 'Setting Camera'))
    sGain = float(cv2.getTrackbarPos('Gain', 'Setting Camera'))
    sExpo = float(cv2.getTrackbarPos('Expo', 'Setting Camera'))
    Setting = np.array([sBri,sCon,sSat,sHue,sGain,sExpo])
    setting=Setting/100

    #print Setting
    #print setting

    cap.set(10,setting[0] )
    cap.set(11,setting[1] )
    cap.set(12,setting[2] )
    #cap.set(13,setting[3] )
    #cap.set(14,setting[4] )
    #cap.set(15,setting[5] )
    
    
    #print bri
    #print cap.get(10)

    blur = cv2.blur(frame,(7,7))
    cv2.imshow('blur',blur)
    cv2.imshow('frame',frame)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
