# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

igv = 0.18
def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1+0.18)
    return subtotal*(1+igv)
# y por qué no poner 1.18?
# Porque si hago cambios solo necesitaría una línea

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)