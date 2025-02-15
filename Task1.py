import json
import random

def kwargsAceeptFun(**Kw):
    for key, val in Kw.items():
        print(f"{key}: {val}")