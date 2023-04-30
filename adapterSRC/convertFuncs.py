import json, xmltodict

def xml2json(driveLocation):
    with open(driveLocation) as xml:
        data = xmltodict.parse(xml.read())
        jsonData = json.dumps(data)
        with open(driveLocation[:-3]+"json", "w") as jsonOut:
            jsonOut.write(jsonData)

xml2json('./adapterSRC/note.xml')