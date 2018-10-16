#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

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

        for linea in etiquetas:
            elemento = linea[0]
            atributos = linea[1]
            print(str(elemento), end='')
            for atributo in atributos:
                if atributos[atributo] != '':
                    print("\\t" + str(atributo) + "=" + '"'
                          + str(atributos[atributo])
                          + '"', end='')
            print('\\n')
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
