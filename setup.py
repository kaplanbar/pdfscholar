from setuptools import setup, find_packages

setup(
    name="pdfscholar",
    version="0.1.0",
    description="Command-line tool for studying PDFs efficiently.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/pdfscholar",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "pypdf>=5.1.0"
    ],
    entry_points={
        "console_scripts": [
            "pdfscholar=pdfscholar.cli:pdfscholar"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
