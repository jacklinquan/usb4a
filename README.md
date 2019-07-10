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

In buildozer.spec add termios.so to the whitelist.

Include usb4a in requirements.

Add intent-filter.xml.

```
# (list) python-for-android whitelist
android.p4a_whitelist = lib-dynload/termios.so

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
requirements = kivy, pyjnius, usb4a

# (str) XML file to include as an intent filters in <activity> tag
android.manifest.intent_filters = intent-filter.xml 
```

Build the project for the first time and it will fail with an error as expected.

`buildozer android debug`

In the generated  `.buildozer` folder find a `res` folder like this one:

`.buildozer/android/platform/build/dists/YOU_PROJECT_NAME/src/main/res`

Create a `xml` folder in `res` folder.

Add device_filter.xml to this `res/xml/` folder.

Find a manifest template file like this one:

`.buildozer/android/platform/build/dists/YOUR_PROJECT_NAME/templates/AndroidManifest.tmpl.xml`

Add  `<uses-feature android:name="android.hardware.usb.host" />`  to this AndroidManifest.tmpl.xml at a good position.

Build the project again and it should pass.
