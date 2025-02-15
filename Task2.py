import json
import random

def typeBasedTransformer(**Kw):
    trans = {}

    for key, val in Kw.items():
        try:
            val = json.loads(val)
        except:
            pass
        if isinstance(val, bool):
            trans[key] = not val
        elif isinstance(val, (int, float)):
            trans[key] = val ** 2
        elif isinstance(val, str):
            trans[key] = val[::-1]
        elif isinstance(val, (list, tuple)):
            reverse = val[::-1]
            trans[key] = type(val)(reverse)
        elif isinstance(val, dict):
            trans[key] = {v: k for k, v in val.items()}
        else:
            trans[key] = val

        return trans