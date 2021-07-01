import xmltodict
import abc


class Parser(metaclass=abc.ABCMeta):
    def __init__(self, file):
        with open(file, 'r') as f:
            self.content = f.read()


class DimacsParser(Parser):
    def __init__(self, file):
        super().__init__(file)


class XMLParser(Parser):
    def __init__(self, file):
        super().__init__(file)
        self.xml = xmltodict.parse(self.content)


class FeatureIDEParser(XMLParser):
    def __init__(self, file):
        super().__init__(file)


class SPLConquerorParser(XMLParser):
    def __init__(self, file):
        super().__init__(file)


class SXFMParser(XMLParser):
    def __init__(self, file):
        super().__init__(file)