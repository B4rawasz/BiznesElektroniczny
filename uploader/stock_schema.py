import random


def toXAMLStockSchema(product_id: int, id: int) -> str:
    quantity = random.randint(0, 10)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <stock_available>
        <id><![CDATA[{id}]]></id>
        <id_product><![CDATA[{product_id}]]></id_product>
        <id_product_attribute><![CDATA[0]]></id_product_attribute>
        <id_shop><![CDATA[1]]></id_shop>
        <id_shop_group><![CDATA[0]]></id_shop_group>
        <quantity><![CDATA[{quantity}]]></quantity>
        <depends_on_stock><![CDATA[0]]></depends_on_stock>
        <out_of_stock><![CDATA[2]]></out_of_stock>
        <location><![CDATA[]]></location>
    </stock_available>
</prestashop>'''
    return xml