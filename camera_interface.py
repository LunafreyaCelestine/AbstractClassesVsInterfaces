from abc import ABC, abstractmethod

class CameraInterface(ABC):
    """
    An interface defining the behavior of camera classes.
    In an interface you don't define the constructor.
    Many languages won't allow concrete methods in an interface.
    Python allows them, but it is not always best practice.
    """
    @abstractmethod
    def capture(self):
        """Method to make the object capture an image"""
        pass

class USBCamera(CameraInterface):
    """
    A concrete class implementing the CameraInterface
    """
    def __init__(self, device):
        self.device # some camera device connected to the computer

    def capture(self):
        img = self.device.capture_img() # made up function for example purposes
        return img


