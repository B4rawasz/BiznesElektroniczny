def toXAMLSaleSchema(product_id: int) -> str:
    xml = f'''<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
  <specific_price>
    <id_shop><![CDATA[1]]></id_shop>
    <id_cart><![CDATA[0]]></id_cart>
    <id_product><![CDATA[{product_id}]]></id_product>
    <id_currency><![CDATA[0]]></id_currency>
    <id_country><![CDATA[0]]></id_country>
    <id_group><![CDATA[0]]></id_group>
    <id_customer><![CDATA[0]]></id_customer>
    <price><![CDATA[-1]]></price>
    <from_quantity><![CDATA[1]]></from_quantity>
    <reduction><![CDATA[0.15]]></reduction>
    <reduction_tax><![CDATA[1]]></reduction_tax>
    <reduction_type><![CDATA[percentage]]></reduction_type>
    <from><![CDATA[0000-00-00 00:00:00]]></from>
    <to><![CDATA[0000-00-00 00:00:00]]></to>
  </specific_price>
</prestashop>

'''
    return xml