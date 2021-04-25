from setuptools import setup

setup(
    name="covid-cli",
    version="0.1",
    py_modules=['cli'],
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
    [console_scripts]
    cli=cli:cli
    '''
)
