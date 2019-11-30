import os
from inspect import signature
import TTS
import webbrowser

path_directory=os.path.dirname(os.path.realpath(__file__))
ParrotToy_path = path_directory + '\ParrotToy_0.1\ParrotToy.py'
ToyPhone_path = path_directory + '\Toyphone_0.2\TOYPHONE.py'



def _get_signature(name_function):
    return str(signature(name_function))


def ParrotToy():
    TTS.talk('Запущен ParrotToy')
    os.system(ParrotToy_path)

def ToyPhone():
    print('Запущен ToyPhone')
    os.system(ToyPhone_path)

def launch_site():
    TTS.talk("Открываю Вконтакте")
    # Указываем сайт для открытия
    url = 'https://vk.com'
    webbrowser.open(url)