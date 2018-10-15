#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.etiqueta =[]

    def startElement(self, name, attrs):
        etiqueta = {'root-layout': {'width', 'height', 'background-color'},
                    'region': {'id', 'top', 'bottom', 'left', 'right'},
                    'img': {'src', 'region', 'begin', 'dur'},
                    'audio': {'src', 'begin', 'dur'},
                    'textstream': {'src', 'region'}}


        if name in etiqueta:
            variables = {}
            for atribute in etiqueta[name]:
                variables[atribute] = attrs.get(atribute, "")

            self.etiqueta.append([name, variables])


    def get_tags(self):
        return self.etiqueta



if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
