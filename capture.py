# Import opencv
import cv2 

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time

labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
#labels = ['thumbsup', 'thumbsdown']
number_imgs = 5
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
#         mkdir -p IMAGES_PATH
        os.makedirs(IMAGES_PATH, exist_ok=True)
    if os.name == 'nt':
        os.mkdir(IMAGES_PATH)
#          mkdir {IMAGES_PATH}
            
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.mkdir(path)
#        mkdir {path}

for label in labels:
    cap = cv2.VideoCapture(0)
    print('Press S to take a picture, ESC to quit')
    print('Collecting images for {}'.format(label))
    time.sleep(3)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        
        #cv2.imshow('frame', frame)
        while(1):
            ret, frame = cap.read()
            
            k = cv2.waitKey(1)
            if k ==27:
                break
            elif k & 0xFF==ord('s'):
                imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
                cv2.imwrite(imgname, frame)
                time.sleep(2)
                break
            cv2.imshow('frame', frame)
        

cap.release()
cv2.destroyAllWindows()