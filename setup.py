from setuptools import setup, find_packages


setup (
    name             = "hello",
    version          = "3.5",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)
