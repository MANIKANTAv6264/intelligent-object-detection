import cv2
import numpy as np

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

def detect_object(frame):
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    detected = []

    for out in outputs:
        for d in out:
            scores = d[5:]
            class_id = int(np.argmax(scores))
            confidence = scores[class_id]
            if confidence > 0.5:
                detected.append(classes[class_id])

    if "cell phone" in detected:
        return "cell phone"
    if detected:
        return detected[0]

    return None
