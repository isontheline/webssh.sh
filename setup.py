from setuptools import setup

setup(
    name='wsh',
    version='0.1.0',
    description='WebSSH Tools Library',
    url='https://github.com/isontheline/webssh.sh',
    author='Arnaud MENGUS',
    license='MIT',
    packages=['wsh'],
    install_requires=[],
    scripts=['wsh/bin/wshcopy'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
