# Kivy is needed for pyjnius behind the scene.
import kivy
from usb4a import usb
from pprint import pprint

usb_device_list = usb.get_usb_device_list()
usb_device_name_list = [device.getDeviceName() for device in usb_device_list]
usb_device_dict = {
    device.getDeviceName():[
        device.getVendorId(), 
        device.getManufacturerName(),
        device.getProductId(),
        device.getProductName()
        ] for device in usb_device_list
    }
pprint(usb_device_dict)
