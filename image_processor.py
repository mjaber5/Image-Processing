import numpy as np
import cv2

class ImageProcessor:
    def __init__(self, kernel_size=(5, 5)):
        self.kernel = np.ones(kernel_size, np.uint8) 

    def erode(self, image):
        return cv2.erode(image, self.kernel)

    def dilate(self, image):
        return cv2.dilate(image, self.kernel)
    
    def open(self, image):
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, self.kernel)
    
    def close(self, image):
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, self.kernel)

    def process(self, image, operation_type):
        operations = {
            'erosion': self.erode,
            'dilation': self.dilate,
            'opening': self.open,
            'closing': self.close
        }
        operation = operations.get(operation_type)
        
        if operation:
            return operation(image)
        raise ValueError(f"Unsupported operation: {operation_type}")
