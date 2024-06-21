import os
import shutil
import cv2
import sys

class FrameCapture:
    def __init__(self, file_path):
        self.directory = 'captured_frames'
        self.file_path = file_path

        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        '''
            Capture frames from video file
        '''
        cv2_object = cv2.VideoCapture(self.file_path)

        fram_number = 0
        frame_found = 1

        while frame_found:
            frame_found, frame = cv2_object.read()
            if frame_found:
                cv2.imwrite(f'{self.directory}/frame_{fram_number}.jpg', frame)
                fram_number += 1

        cv2_object.release()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python capture_video_frames.py <video_file_path>')
        sys.exit(1)

    video_file_path = sys.argv[1]
    frame_capture = FrameCapture(video_file_path)
    frame_capture.capture_frames()
    print('Frames captured successfully!')
