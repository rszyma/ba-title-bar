import cv2

# used to scale down the video resolution
 
# the repo doesn't include vid 480x360 file, 
# but you can get it yourself e.g. using this youtube-dl command:
# youtube-dl -f 18 'https://www.youtube.com/watch?v=FtutLA63Cp8' -o bad_apple_480x360.mp4

cap = cv2.VideoCapture('bad_apple_480x360.mp4')

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('bad_apple_48x36.mp4', fourcc, 30, (48, 36)) # output: 30 fps, 48x36

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, (48, 36), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
        out.write(b)
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()