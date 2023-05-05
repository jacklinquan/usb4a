# usb4a
[![PyPI version](https://badge.fury.io/py/usb4a.svg)](https://badge.fury.io/py/usb4a) [![Downloads](https://pepy.tech/badge/usb4a)](https://pepy.tech/project/usb4a)

Python package for Android USB host.

Please try the Android App built with usb4a on Google Play: [PyTool USB Serial Free](https://play.google.com/store/apps/details?id=com.quanlin.pytoolusbserialfree).

Please consider [![Paypal Donate](https://github.com/jacklinquan/images/blob/master/paypal_donate_button_200x80.png)](https://www.paypal.me/jacklinquan) to support me.

**Android platform related classes:**

PythonActivity

Context

Intent

PendingIntent

**USB related classes:**

UsbConstants

UsbRequest

USBError

**Helper classes:**

ByteBuffer

**Helper functions:**

get_usb_manager

get_usb_device_list

get_usb_device

has_usb_permission

request_usb_permission

build_usb_control_request_type

arraycopy


This package can be used for implementing USB device driver for Android USB host, like USB serial port drivers.

## How to use it:
**If not in need to build a dedicated app:**

It works for Android 6.0+.

Get Pydroid apps from [here](https://github.com/jacklinquan/Pydroid_Apks).

Or get the latest versions on [Google Play](https://play.google.com/store/apps).

In Pydroid, go to Menu->Pip.

Install usb4a.

Open `example.py` and run it.

Go to Menu->Graphical program output.

Scroll to the last line, it should list all the USB devices connected to the Android phone/tablet with vendor id, vendor name, product id and product name.

**If a dedicated app is needed to be built with buildozer:**

It works for Android 4.0+.

Grab the contents of the `xml/` folder within this repo. Put them into a similar folder within your project.
The files work as they are. It is recommended to run the app first without modifying them. They can later
be modified as deemed suitable.

**Modify the buildozer.spec:**

In buildozer.spec add termios.so to the whitelist.

Include usb4a in requirements.

```
# (list) python-for-android whitelist
android.p4a_whitelist = lib-dynload/termios.so

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
requirements = kivy, pyjnius, usb4a

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
android.extra_manifest_xml = manifest/extra_manifest.xml

# (str) XML file to include as an intent filters in <activity> tag
android.manifest.intent_filters = manifest/intent-filter.xml

# (list) Copy these files to src/main/res/xml/ (used for example with intent-filters)
android.res_xml = manifest/device_filter.xml
```

Thats it, build the app and deploy it, everything should work now
