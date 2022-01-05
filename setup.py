from setuptools import setup, find_packages


setup (
    name             = "Python",
    version          = "1.0",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)
