from __future__ import print_function
import yaml

def loadCredentials():
    doc = []
    with open("/home/settings.yaml", 'r') as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    return doc
