import json, xmltodict, sys, csv

def xml2json(driveLocation):
    with open(driveLocation) as xml:
        data = xmltodict.parse(xml.read())
        jsonData = json.dumps(data)
        with open(driveLocation[:-3]+"json", "w") as jsonOut:
            jsonOut.write(jsonData)

def csv2json(driveLocation):
    out = []
    with open(driveLocation) as csvIn:
        data = csv.DictReader(csvIn)
        for rows in data:
            out.append(rows)
    with open(driveLocation[:-3]+"json", "w") as jsonOut:
        jsonOut.write(json.dumps(out, indent=4))

sys.modules[__name__] = xml2json

xml2json('./note.xml')
csv2json('./addresses.csv')
