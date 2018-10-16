#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

import json
import sys
if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        fichero = sys.argv[1]

        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))

        etiquetas = cHandler.get_tags()

        nombre_json = fichero[:-4] + 'json'
        fichero_json = open(nombre_json, 'w')
        for linea in etiquetas:
            elemento = linea[0]
            atributos = linea[1]
            print(str(elemento), end='')
            json.dump(elemento, fichero_json)
            for atributo in atributos:
                if atributos[atributo] != '':
                    json.dump("\t" + atributo + "="
                              + (atributos[atributo]), fichero_json)

                    print("\\t" + str(atributo) + "=" + '"'
                          + str(atributos[atributo])
                          + '"', end='')
            json.dump('\n', fichero_json)
            print('\\n')

    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
