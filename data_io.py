import yaml
import os

FILE = os.path.join(os.getcwd(), 'data.yml')


def read_yaml(data_file=FILE):
    with open(data_file, 'r') as fp:
        documents = yaml.load(fp)
        # print(documents.keys())
        # TODO: verify document types
        if 'food' and 'activities' not in documents.keys():
            return 'Bad keys. Incorrectly formatted data! Try again?'

    return documents


def instantiate_yaml_documents(read_output):
    for item, doc in read_output.items():
        print(item, ":", doc)

    return 0
