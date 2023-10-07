from setuptools import setup

setup(
    name="wayfinder-aus",
    version="0.1",
    description="Using the Google Maps SDK to help rental searches.",
    author="Christopher Khoo",
    author_email="khoojinnwei@gmail.com",
    packages=[
        "builder",
        "builder.constants",
        "builder.data",
        "builder.helpers",
        "builder.core",
        "builder.service"
    ]
)