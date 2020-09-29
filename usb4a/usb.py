'''USB module for Android

Android platform related classes:
PythonActivity
Context
Intent
PendingIntent

USB related classes:
UsbConstants
UsbRequest
USBError

Helper classes:
ByteBuffer

Helper functions:
get_usb_manager
get_usb_device_list
get_usb_device
has_usb_permission
request_usb_permission
build_usb_control_request_type
arraycopy
'''

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
PythonService = autoclass('org.kivy.android.PythonService')
Context = autoclass('android.content.Context')
Intent = autoclass('android.content.Intent')
PendingIntent = autoclass('android.app.PendingIntent')

UsbConstants = autoclass('android.hardware.usb.UsbConstants')
UsbRequest = autoclass('android.hardware.usb.UsbRequest')

ByteBuffer = autoclass('java.nio.ByteBuffer')

USB_RECIPIENT_DEVICE = 0x00
USB_RECIPIENT_INTERFACE = 0x01
USB_RECIPIENT_ENDPOINT = 0x02
USB_RECIPIENT_OTHER = 0x03


class USBError(IOError):
    '''USB Error class'''

def get_context():
    '''Get the mActivity or mService context depending on what is available'''
    if PythonActivity.mActivity:
        context = PythonActivity.mActivity
    elif PythonService.mService:
        context = PythonService.mService
    else:
        raise RuntimeError("Could not resolve context")
    return context

def get_usb_manager():
    '''Get USB manager object from the system.
    
    Returns:
        usb_manager: an object representing USB manager from the system.  
    '''
    usb_manager = get_context().getSystemService('usb')
    return usb_manager

def get_usb_device_list():
    '''Get USB device list.
    
    Returns:
        usb_device_list: a list of existing USB devices
    
    Example:
        usb_device_list = get_usb_device_list()
        usb_device_list[0].getDeviceName()
        usb_device_list[0].getVendorId()
        usb_device_list[0].getManufacturerName()
        usb_device_list[0].getProductId()
        usb_device_list[0].getProductName()
    '''
    usb_manager = get_usb_manager()
    usb_device_list = usb_manager.getDeviceList().values().toArray()
    return usb_device_list
    
def get_usb_device(device_name):
    '''Get a USB device object from the system.
    
    Parameters:
        device_name (str): the name of the USB device.
    
    Returns:
        usb_device: an object representing the USB device.  
    '''
    usb_device_list = get_usb_device_list()
    for usb_device in usb_device_list:
        if usb_device and usb_device.getDeviceName()==device_name:
            return usb_device
    return None

def has_usb_permission(usb_device):
    '''Test if permission is granted for the given USB device.
    
    Parameters:
        usb_device (object): the USB device object.
    
    Returns:
        boolean: True if permission is granted, otherwise False.  
    '''
    usb_manager = get_usb_manager()
    return usb_manager.hasPermission(usb_device)
    
def request_usb_permission(usb_device):
    '''Request permission for the given USB device.
    
    Parameters:
        usb_device (object): the USB device object. 
    '''
    usb_manager = get_usb_manager()
    ACTION_USB_PERMISSION = "com.access.device.USB_PERMISSION"
    intent = Intent(ACTION_USB_PERMISSION)
    pintent = PendingIntent.getBroadcast(get_context(), 0, intent, 0)
    usb_manager.requestPermission(usb_device, pintent)
    
def build_usb_control_request_type(direction, usb_type, recipient):
    '''Build USB control request type for USB communication.
    
    Parameters:
        direction (int):
        usb_type (int):
        recipient (int):
    
    Returns:
        request type (int):
    '''
    return direction | usb_type | recipient

def arraycopy(source, sourcepos, dest, destpos, numelem):
    '''Python version of System.arraycopy() in Java.
    
    Parameters:
        source (list): source list to copy from.
        sourcepos (int): the position in source list to start copying.
        dest (list): destination list to copy to.
        destpos (int): the position in destination list to start copying.
        numelem (int): the data length to copy.
    '''
    dest[destpos:destpos+numelem] = source[sourcepos:sourcepos+numelem]    
