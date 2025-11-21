def toXAMLManufacturerSchema(name):
    link_rewrite = name.lower().replace(' ', '-')
    link_rewrite = ''.join(c for c in link_rewrite if c.isalnum() or c == '-')

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <manufacturer>
        <name><![CDATA[{name}]]></name>
        <active><![CDATA[1]]></active>
    </manufacturer>
</prestashop>
'''
    
    return xml