#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from gi.repository import Gtk


class Compilador:
    def __init__(self):
        self.gui = Gtk.Builder()

    self.gui.add_from_file("gui2.glade")
    senales = {'on_salir': Gtk.main_quit,
               'on_compilar': self.compilar,
               'on_conf_len': self.configurarLenguaje,
               'on_acept_len': self.aceptarLenguaje,
               'on_cancel_len': self.cancelLenguaje,
               'on_conf_pal': self.configurarPalabras,
               'on_acept_pal': self.aceptarPalabras,
               'on_cancel_pal': self.cancelPalabras,
               'on_len_def': self.lenguajeDefault, }
    self.gui.connect_signals(senales)


self.caracteres = "qwertyuiopasdfghjklñmnbvcxz,;.:áéíóú1234567890() \n \t '"
self.palabras_reservadas = ['for', 'in', 'def', 'False', 'True', 'if', 'else', 'elif', 'try', 'except', 'class', 'and',
                            'or', 'not', 'print', 'range', '\t', '\n', '']

self.texto_principal = self.gui.get_object("TxtViewPrincipal")
self.texto_mensajes = self.gui.get_object("TxtViewMensajes")
self.texto_lenguaje = self.gui.get_object("TxtViewLen")
self.texto_lenguaje2 = self.gui.get_object("TxtViewLen1")
self.ventana_dialogo = self.gui.get_object("dialog1")
self.ventana_dialogo2 = self.gui.get_object("dialog2")


def lenguajeDefault(self, widget):
    self.caracteres = "qwertyuiopasdfghjklñmnbvcxz,;.:áéíóú1234567890() \n \t '"


def aceptarPalabras(self, widget):
    texto_len = self.texto_lenguaje2.get_buffer()


self.palabras_reservadas = texto_len.get_text(texto_len.get_start_iter(), texto_len.get_end_iter(), False).split(" ")
self.palabras_reservadas.extend("\t\n ")
self.ventana_dialogo2.hide()


def aceptarLenguaje(self, widget):
    texto_len = self.texto_lenguaje.get_buffer()


self.caracteres = texto_len.get_text(texto_len.get_start_iter(), texto_len.get_end_iter(), False) + "\n \t "
self.ventana_dialogo.hide()


def cancelLenguaje(self, widget):
    self.ventana_dialogo.hide()
