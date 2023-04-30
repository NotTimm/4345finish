import json, xmltodict, sys

def xml2json(driveLocation):
    with open(driveLocation) as xml:
        data = xmltodict.parse(xml.read())
        jsonData = json.dumps(data)
        with open(driveLocation[:-3]+"json", "w") as jsonOut:
            jsonOut.write(jsonData)

sys.modules[__name__] = xml2json

xml2json('./adapterSRC/note.xml')