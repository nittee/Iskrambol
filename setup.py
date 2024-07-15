'''
Iskrambol
'''

from setuptools import setup

# external packages as dependencies
install_reqs = []
with open('requirements.txt', 'r') as file_reqs:
    for line in file_reqs:
        install_reqs.append(line)

with open("README", 'r') as file_readme:
    long_description = file_readme.read()

setup(
    name='iskrambol',
    version='0.0.0',
    description=(
        "A wireless local PvP multiplayer word game designed to gauge the "
        "players' vocabulary knowledge while racing against other players "
        "or against time (single-player mode)."
    ),
    license="",     # TODO
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nittee Pards',
    author_email='foomail@foo.example',     # TODO
    url="https://github.com/nittee/Iskrambol",
    packages=[
        'iskrambol',
    ],
    install_requires=install_reqs, 
    scripts=[
        'utils/',
    ]
)
