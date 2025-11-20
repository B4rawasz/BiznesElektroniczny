

def toXAMLCategorySchema(category: str, description: str, id_parent: int | None) -> str:
    # Generowanie link_rewrite - zamiana na lowercase i spacje na myślniki
    link_rewrite = category.lower().replace(' ', '-')
    # Usunięcie znaków specjalnych
    link_rewrite = ''.join(c for c in link_rewrite if c.isalnum() or c == '-')
    
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
<category>
    <name>
        <language id="1"><![CDATA[{category}]]></language>
    </name>
    <link_rewrite>
        <language id="1"><![CDATA[{link_rewrite}]]></language>
    </link_rewrite>
    <description>
        <language id="1"><![CDATA[{description}]]></language>
    </description>
    <active>1</active>
    {id_parent is None and '' or f'<id_parent>{id_parent}</id_parent>'}
</category>
</prestashop>'''
    
    return xml