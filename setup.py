from setuptools import setup

setup(
    name="usb4a",
    version="0.1.0",
    description="Python package for Android USB host.",
    url="https://github.com/jacklinquan/usb4a",
    author="Quan Lin",
    author_email="jacklinquan@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    packages=["usb4a"],
    install_requires=["kivy", "pyjnius"]
    )
