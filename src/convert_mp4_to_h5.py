import h5py
from cv2 import VideoCapture
# from skvideo.io import VideoCapture
frames = []
cap = VideoCapture('/home/ofersabo/EVE/data/my_own_data/999_video/step_0/Session_05599f54-0004-4961-aa36-e53b70b3ff2b_recording.mp4')
cap.open(0)

output_file = "/home/ofersabo/EVE/data/my_own_data/999_video/webcam_c.h5"

it = 0
while True:
    retval, image = cap.read()
    if image != None:
        frames.append(image)
        it += 1
        if (it % 1000 == 0):
            print('Processed %d frames so far' % (it))
    if not retval:
        break

with h5py.File(output_file,'w') as h5File:
    h5File.create_dataset('camera1',data=frames,compression='gzip',compression_opts=9)