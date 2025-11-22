def toXAMLManufacturerSchema(name):
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <manufacturer>
        <name><![CDATA[{name}]]></name>
        <active><![CDATA[1]]></active>
    </manufacturer>
</prestashop>
'''
    
    return xml