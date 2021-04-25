from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name="covid-cli",
    version="1.0.0",
    author="sumit kushwah",
    author_email="sumitkushwah1729@gmail.com",
    url="https://github.com/sumit-kushwah/covid-cli",
    description="Cli app for covid statistics and history.",
    long_description=long_description,
    long_description_content_type ="text/markdown",
    license="MIT",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={  # Optional
        'console_scripts': [
            'covid=scripts:cli',
        ],
    },
    classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    keywords ='covid cli-app',
    install_requires = requirements,
    zip_safe = False
)
