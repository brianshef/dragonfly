from setuptools import setup, find_packages

setup(
    name="dragonfly",
    version="1.2.0",
    author="Brian Shef",
    author_email="brianshef@gmail.com",
    description="A Markov Chain generator based on artist lyrics and wiki pages",
    url="https://github.com/brianshef/dragonfly",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    # scripts=['main.py'],
    entry_points={
        'console_scripts': ['dragonfly=dragonfly.main:main']
    },
)
