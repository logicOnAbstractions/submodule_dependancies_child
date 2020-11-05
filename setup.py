import setuptools


# This call to setup() does all the work
setuptools.setup(
    name="commonlib",
    version="0.0.1",
    description="A simple Python package",
    long_description="a longer description of the same thingy",
    long_description_content_type="text/x-rst",
    author="Author Name",
    author_email="author@email.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7"
)