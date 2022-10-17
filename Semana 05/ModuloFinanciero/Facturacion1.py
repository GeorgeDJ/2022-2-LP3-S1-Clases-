# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:21:33 2022

@author: ACER
"""

#Dado el subtotal, calcular el IGV y el Total

import Financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {Financieros.obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total: {Financieros.obtenerTotalconSubtotal(subtotal):.2f}")