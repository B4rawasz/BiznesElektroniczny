import random


def toXAMLProductSchema(manufacturer_id: int | None, price: float, name: str, description: str, short_description: str, category_id: int, code: str) -> dict:
    on_sale = random.choices([1, 0], weights=[20, 80], k=1)[0]
    new = random.choices([1, 0], weights=[10, 90], k=1)[0]
    weight = round(random.uniform(0.5, 8.0), 2)

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
<product>
    {manufacturer_id is None and '' or f'<id_manufacturer><![CDATA[{manufacturer_id}]]></id_manufacturer>'}
    <id_category_default><![CDATA[{category_id}]]></id_category_default>
    <new><![CDATA[{new}]]></new>
    <id_tax_rules_group><![CDATA[1]]></id_tax_rules_group>
    <price><![CDATA[{round(price / 1.23, 2)}]]></price>
    <active><![CDATA[1]]></active>
    <weight><![CDATA[{weight}]]></weight>
    <on_sale><![CDATA[{on_sale}]]></on_sale>
    <reference><![CDATA[{code}]]></reference>
    <state><![CDATA[1]]></state>
    <minimal_quantity><![CDATA[1]]></minimal_quantity>
    <redirect_type>><![CDATA[404]]></redirect_type>
    <available_for_order><![CDATA[1]]></available_for_order>
    <show_price><![CDATA[1]]></show_price>
    <pack_stock_type><![CDATA[3]]></pack_stock_type>
    <name>
        <language id="1"><![CDATA[{name}]]></language>
    </name>
    <description>
        <language id="1"><![CDATA[{description}]]></language>
    </description>
    <description_short>
        <language id="1"><![CDATA[{short_description}]]></language>
    </description_short>
    <associations>
        <categories>
            <category>
                <id><![CDATA[{category_id}]]></id>
            </category>
            <category>
                <id><![CDATA[2]]></id>
            </category>
        </categories>
    </associations>
</product>
</prestashop>
'''
    ret = {}
    ret['xml'] = xml
    ret['on_sale'] = bool(on_sale)
    return ret