#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="dash-create", # Replace with package name

    version="1.0.0",

    author="Ken Trinh",

    author_email="ktrinh.particle@gmail.com",

    description="fullstack python dash application filestructure",

    long_description_content_type="text/markdown",

    url="https://github.com/CVolticz/dash-create.git",

    packages=setuptools.find_packages(include=['dash_create', 'dash_create.*', 'dash_create.bin']),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    entry_points={
        'console_scripts': ['dash-create=dash_create.fs_builder:main'],
    },

    install_requires=['click',
                    'pandas', 
                    'numpy', 
                    'scipy',
                    'matplotlib', 
                    'seaborn',
                    'dash==2.0.0', 
                    'plotly>=5.0.0', 
                    'dash-bootstrap-components',
                    'waitress==1.4.0',
                    'requests',
                ],

    python_requires='>=3.7',

)
