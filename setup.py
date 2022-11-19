from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='webssh-sh',
    version='22.11.1',
    description='Shell Helpers about WebSSH',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
