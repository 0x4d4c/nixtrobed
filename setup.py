from setuptools import setup, find_packages

setup(
    name="nixtrobed",
    version="0.1.0",
    license="MIT",
    author="Martin Lambertz",
    author_email="martin@0x4d4c.xyz",
    url="https://github.com/0x4d4c/nixtrobed",
    packages=find_packages(),
    install_requires=[
        "ansible",
        "click",
        "jinja2",
        "python-vagrant",
    ],
    entry_points={"console_scripts": ["nixtrobed = nixtrobed.__main__:main"]},
    description="A simple app to generate testbeds for different Linux and BSD distros",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Source": "https://github.com/0x4d4c/nixtrobed",
        "Tracker": "https://github.com/0x4d4c/nixtrobed/issues",
    },
    python_requires=">3.8",
)
