# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:28:58 2022

@author: ACER
"""

#Dado el total, calcular el IGV y el Subtotal

import Financieros

total = 1000.49
print(f"Subtotal: {Financieros.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV: {Financieros.obtenerIGVconTotal(total):.2f}")
print(f"Total: {total}")