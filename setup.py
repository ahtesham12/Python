from setuptools import setup, find_packages


setup (
    version          = "1.0",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)
