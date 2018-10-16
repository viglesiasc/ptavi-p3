#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve

import json
import sys


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))

        self.etiquetas = cHandler.get_tags()

    def __str__(self):
        for linea in self.etiquetas:
            elemento = linea[0]
            atributos = linea[1]
            print(str(elemento), end='')

            for atributo in atributos:

                if atributos[atributo] != '':
                    print("\\t" + str(atributo) + "=" + '"'
                          + str(atributos[atributo])
                          + '"', end='')
            print('\\n')

    def to_json(self, fichero_json):
        fichero_json = open(nombre_json, 'w')
        for linea in self.etiquetas:
            elemento = linea[0]
            atributos = linea[1]

            json.dump(elemento, fichero_json)
            for atributo in atributos:

                if atributos[atributo] != '':
                    json.dump("\t" + atributo + "="
                              + (atributos[atributo]), fichero_json)
            json.dump('\n', fichero_json)

    def do_local(self):
        for linea in self.etiquetas:
            elemento = linea[0]
            atributos = linea[1]
            for atributo in atributos:
                if atributo == 'src' and atributos[atributo][0:7] == 'http://':
                    urlretrieve(atributos[atributo],
                                atributos[atributo].split('/')[-1])
                    atributos[atributo] = atributos[atributo].split('/')[-1]

if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        fichero = sys.argv[1]
        nombre_json = fichero[:-4] + 'json'
        karaoke = KaraokeLocal(fichero)     # b
        karaoke.__str__()   # c
        karaoke.to_json(nombre_json)     # d
        karaoke.do_local()  # e
        karaoke.to_json('local')    # f
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
