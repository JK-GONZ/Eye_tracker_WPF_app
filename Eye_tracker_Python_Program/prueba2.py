'''
from ultralytics import YOLO
from ultralytics.yolo import DetectionPredictor





model = YOLO("best.pt")

result = model.predict(source=0, show=True)


print(result)


'''



'''
    Ejecucion en gitBash para probar modelos con webcam y Yolov5:
        python detect.py --weights best.py --source 0
'''

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
# imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

# os.system("python ./Yolov5/yolov5/detect.py --weights ./Yolov5/yolov5/runs/detect/exp/best.pt --source 0")

import cv2
import torch
from torch import hub # Hub contains other models like FasterRCNNmodel = torch.hub.load( \'ultralytics/yolov5', \'yolov5s', \pretrained=True)
import time
import numpy as np

# Model
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, etc.
# model = torch.hub.load('ultralytics/yolov5', 'custom', './Yolov5/yolov5/runs/detect/exp/best.pt')  # custom trained model
# model = torch.hub.load('ultralytics/yolov5', 'custom', './Yolov5/yolov5/runs/detect/exp/best.pt')






"""
The function below identifies the device which is availabe to make the prediction and uses it to load and infer the frame. Once it has results it will extract the labels and cordinates(Along with scores) for each object detected in the frame.
"""
def score_frame(frame, model):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)
    frame = [torch.tensor(frame)]
    results = model(frame)
    labels = results.xyxyn[0][:, -1].numpy()
    cord = results.xyxyn[0][:, :-1].numpy()
    return labels, cord


"""
The function below takes the results and the frame as input and plots boxes over all the objects which have a score higer than our threshold.
"""
def plot_boxes(self, results, frame):
    labels, cord = results
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    for i in range(n):
        row = cord[i]
        # If score is less than 0.2 we avoid making a prediction.
        if row[4] < 0.2: 
            continue
        x1 = int(row[0]*x_shape)
        y1 = int(row[1]*y_shape)
        x2 = int(row[2]*x_shape)
        y2 = int(row[3]*y_shape)
        bgr = (0, 255, 0) # color of the box
        classes = self.model.names # Get the name of label index
        label_font = cv2.FONT_HERSHEY_SIMPLEX #Font for the label.
        cv2.rectangle(frame, \
                    (x1, y1), (x2, y2), \
                    bgr, 2) #Plot the boxes
        cv2.putText(frame,\
                    classes[labels[i]], \
                    (x1, y1), \
                    label_font, 0.9, bgr, 2) #Put a label over box.
        return frame
    

"""
The Function below oracestrates the entire operation and performs the real-time parsing for video stream.
"""
def __call__(self):
    player = self.get_video_stream() #Get your video stream.
    assert player.isOpened() # Make sure that their is a stream. 
    #Below code creates a new video writer object to write our
    #output stream.
    x_shape = int(player.get(cv2.CAP_PROP_FRAME_WIDTH))
    y_shape = int(player.get(cv2.CAP_PROP_FRAME_HEIGHT))
    four_cc = cv2.VideoWriter_fourcc(*"MJPG") #Using MJPEG codex
    # out = cv2.VideoWriter(out_file, four_cc, 20, \
    #                        (x_shape, y_shape)) 
    ret, frame = player.read() # Read the first frame.
    while ret: # Run until stream is out of frames
        start_time = time() # We would like to measure the FPS.
        results = self.score_frame(frame) # Score the Frame
        frame = self.plot_boxes(results, frame) # Plot the boxes.
        end_time = time()
        fps = 1/np.round(end_time - start_time, 3) #Measure the FPS.
        print(f"Frames Per Second : {fps}")
        cv2.imshow(frame)
        #out.write(frame) # Write the frame onto the output.
        ret, frame = player.read() # Read next frame.



if __name__ == '__main__':
    model = torch.hub.load( 'ultralytics/yolov5', 'custom', './Yolov5/yolov5/runs/detect/exp/best.pt')
    __call__()