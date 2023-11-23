import xml.etree.ElementTree as ElementTree


class XmlHandler:
    def __init__(self, xml_file_path):
        self.tree = ElementTree.parse(xml_file_path)
        self.root = self.tree.getroot()

    def xml_to_string(self):
        return ElementTree.tostring(self.root).decode("utf-8")

    def string_to_xml(self, xml_string):
        return ElementTree.fromstring(xml_string)

    def perform_xml_operations(self):
        first_decade = self.root.find('.//decade[1]')
        new_element = ElementTree.Element("new_element")
        new_element.text = "Hello, World!"
        first_decade.append(new_element)


if __name__ == "__main__":
    xml_handler = XmlHandler("example.xml")

    xml_string = xml_handler.xml_to_string()
    print("XML to String:")
    print(xml_string)

    decoded_xml = xml_handler.string_to_xml(xml_string)
    print("\nString to XML:")
    print(ElementTree.tostring(decoded_xml).decode("utf-8"))

    xml_handler.perform_xml_operations()

    # Виведення зміненого XML після додавання нового елемента
    updated_xml_string = xml_handler.xml_to_string()
    print("\nUpdated XML:")
    print(updated_xml_string)
