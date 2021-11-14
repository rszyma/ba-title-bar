import time
import pyglet
import multiprocessing
import cv2
# import simpleaudio as sa

# 48 x 36
PIXELS_WIDTH = 48
PIXELS_HEIGHT = 36
PIXEL_OFF = "\u2588\u2003"
PIXEL_ON = "   \u2003\u200a"

def create_window(queue, i):
    window = pyglet.window.Window(1275, 0, PIXEL_ON * PIXELS_WIDTH)
    window.set_location(270, 23*i + 30)

    while True:
        pyglet.clock.tick()

        for window in pyglet.app.windows:
            window.dispatch_events()

            msg = queue.get()
            line = "".join([PIXEL_ON if val else PIXEL_OFF for val in msg])
            window.set_caption(line)

def main():
    # init windows
    queue_ps = [] # (queue, process)
    for i in range(PIXELS_HEIGHT):
        start = time.time()
        # queue
        q = multiprocessing.Queue(1)
        p = multiprocessing.Process(target=create_window, args=(q, i))
        queue_ps.append((q, p))
        p.start()
        
        # need some delay, else the windows will appear randomly stacked
        remaining = max(1/(2.3*2) - (time.time() - start), 0)
        time.sleep(remaining)
        

    # prepare sound and video
    cap = cv2.VideoCapture("bad_apple_48x36.mp4")

    # If you want the sound, you can get it your self from https://www.youtube.com/watch?v=FtutLA63Cp8
    ## filename = 'bad_apple.wav' 
    ## wave_obj = sa.WaveObject.from_wave_file(filename)
    time.sleep(6)
    ## wave_obj.play()

    start = time.time()

    # process the video
    while True:
        frame_start = time.time()
        cap.set(cv2.CAP_PROP_POS_MSEC, (time.time() - start) * 1000)
        returned, frame = cap.read()
        if returned == True:
            # render a preview
            double_frame = cv2.resize(frame, (96, 72), fx=0, fy=0)
            cv2.imshow('frame', double_frame)
            cv2.waitKey(1)

            for y in range(0, PIXELS_HEIGHT):
                line = [1 if frame[y, x, 1] > 127 else 0 for x in range(0, PIXELS_WIDTH)] # 0/1 threshold
                queue_ps[y][0].put(line) 
        else:
            for y in range(0, PIXELS_HEIGHT):
                queue_ps[y][0].put(None) # causes some errors and therefore exits the processes :)
            cv2.destroyAllWindows()
            cap.release()
            break
        try:
            print("FPS: ", int(1 / (time.time() - frame_start)))
        except ZeroDivisionError:
            pass
            

if __name__ == "__main__":
    main()

