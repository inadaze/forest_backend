""" Setup for forest_backend """
from setuptools import setup

setup(
    name='forest_backend',
    version='1.0',
    description='Backend database and rest api for the forest game',
    author='Jay Smalridge',
    author_email='jsmalridge@gmail.com',
    packages=['forest_backend'],
    install_requires=[], #external packages as dependencies
    scripts=['forest_backend/database/reset_database.py']
)
