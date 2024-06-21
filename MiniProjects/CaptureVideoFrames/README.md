# In Order to Capture Video Frames

## 1. Install OpenCV

```bash
pip install opencv-python
```

## 2. Capture Video Frames

```python
import cv2

video = cv2.VideoCapture('video.mp4')
success, image = video.read()
count = 0

while success:
    cv2.imwrite(f'frame_{count}.jpg', image)
    success, image = video.read()
    count += 1
```

## 3. Display Video Frames

```python
import cv2

video = cv2.VideoCapture('video.mp4')

while True:
    success, image = video.read()
    if not success:
        break
    cv2.imshow('Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```
