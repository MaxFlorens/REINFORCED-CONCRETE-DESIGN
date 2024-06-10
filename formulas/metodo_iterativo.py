import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.datos import pedir_parametros 

def MetodoIterativo():
    print(pedir_parametros())

MetodoIterativo()


