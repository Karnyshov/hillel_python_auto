from xml.etree import ElementTree

tree = ElementTree.parse("movies.xml")
root = tree.getroot()
genres = root.findall("genre")

for genre in genres:
    for decade in genre.findall("decade"):
        for movie in decade.findall("movie"):
            print(movie.attrib["title"])
