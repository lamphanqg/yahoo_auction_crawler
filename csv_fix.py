# -*- coding: utf-8 -*-
with open("products.csv", "rb") as f:
    with open("products_fixed.csv", "w", encoding='utf8') as f2:
        f2.write(f.read().decode().replace("\r", ""))