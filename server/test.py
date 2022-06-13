import torch

model = torch.hub.load('yolov5', 'yolov5s', source='local')

# Images
img = 'https://images.unsplash.com/photo-1554151228-14d9def656e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8cGVyc29ufGVufDB8fDB8fA%3D%3D&w=1000&q=80'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.show()