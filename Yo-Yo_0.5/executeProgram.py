import os
from inspect import signature

path_directory=os.path.dirname(os.path.realpath(__file__))
ParrotToy_path = path_directory + '\ParrotToy_0.1\ParrotToy.py'
ToyPhone_path = path_directory + '\Toyphone_0.2\TOYPHONE.py'

def talk(x):
    pass


def _get_signature(name_function):
    return str(signature(name_function))


def ParrotToy():
    print(ParrotToy_path)
    os.system(ParrotToy_path)

def ToyPhone():
    print(ToyPhone_path)
    os.system(ToyPhone_path)

ToyPhone()