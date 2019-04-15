import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_operators",
    version="0.0.1",
    author="William Cæsar",
    author_email="williamcaesar@pm.me",
    description="A library to perform math operations with time and timezones",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/williamcaesar/Time-Operators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
)