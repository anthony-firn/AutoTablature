from lxml import etree as et

class Parse(object):
    def __init__(self, filename):
        f = open(filename, "r")
        if f.mode == "r":
            self.filename = filename
            musicXML = f.read().encode()
            self.root = et.fromstring(musicXML)

    def getChildren(self, parent):
        arr = []
        for child in parent:
            arr.append(child)

        return arr

    def printSubTree(self, subRoot, depth):
        print(depth, end="")
        for x in range(depth):
            print("  ", end="")

        print(subRoot.tag, subRoot.attrib, subRoot.text)
        arr = self.getChildren(subRoot)
        for child in arr:
            self.printSubTree(child, depth+1)

    def printTree(self):
        self.printSubTree(self.root, 0)


if __name__ == "__main__":
    # Parse().main()
    parse = Parse("/Users/anthony/Documents/MuseScore3/Scores/Test.musicxml")
    parse.printTree()
