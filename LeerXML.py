import xml.sax

from xml.etree.ElementTree import parse
xml_doc=parse('note.xml')
for ele in xml_doc.findall('pro'):
    print(ele.text)





"""from xml.dom.minidom import parse,Node
xmltree=parse('note.xml')

for nodo in xmltree.getElementsBygTaName('pro'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodoType==Node.TEXT_NODE:
            print(nodo_hijo.data)"""