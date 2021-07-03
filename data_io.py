import yaml
import os

FILE = os.path.join(os.getcwd(), 'data.yml')

def read_yaml(data_file=FILE):
    with open(data_file, 'r') as fp:
        documents = yaml.load(fp)

        # TODO: verify document types
ß
        # for item, doc in documents.items():
        #     print(item, ":", doc)

    return documents