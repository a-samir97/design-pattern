import json
import xml.etree.ElementTree as etree


class JSONConnector:
    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(file_path):
    if file_path.endswith('json'):
        connector = JSONConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(file_path))
    return connector(file_path)


def connect_to(file_path):
    factory = None
    try:
        factory = connection_factory(file_path)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    xml_factory = connect_to('data/person.xml')
    json_factory = connect_to('data/person.json')

    for factory in (sqlite_factory, xml_factory, json_factory):
        print(factory)
