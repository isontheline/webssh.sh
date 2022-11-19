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
    scripts=[],
    entry_points={
        'console_scripts': ['wshcopy=wsh.wshcopy:cli'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
