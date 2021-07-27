#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- Un registro: Convierta el nombre de host a IP.

- Registro MX: Registro de intercambio de correo, que define el nombre de dominio del servidor de correo.

- Registro CHAME: Se refiere a registros de alias para realizar el mapeo entre nombres de dominio.

- Registro NS: Marque el servidor de nombres de dominio de la zona y el subdominio autorizado.

- Registro PTR: La resolución inversa, a diferencia del registro A, convierte la IP en nombre de host.

- Registro SOA: Marca SOA, una definición de zona de autorización inicial.
"""

import dns.resolver

domain = input('Input an domain: ')

A = dns.resolver.query(domain, 'A')

for i in A.response.answer:
    for j in i.items:
        print(j.address)


