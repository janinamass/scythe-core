import json
import os
import sys
from pprint import pprint
from scythecore_context import scythecore


def test_numbers_3_4():
    assert( 3*4 == 12 )


def paths():
        a_f = os.path.abspath(__file__)
        a_s = os.path.abspath(sys.argv[0])

        print ("abs __file__: %s" % a_f)
        print ("abs sys.argv: %s" % a_s)


class Gene(object):
    def __init__(self, species, name, alias=None):
        self.species = species
        self.name = name
        self.alias = alias

class Transcript(object):
    def __init__(self, gene, name, alias=None):
        self.gene = gene
        self.name = name
        self.alias = alias

class Orthogroup(object):
    def __init__(self, genes, name, alias=None):
        self.genes = [g for g in genes if isinstance(g,Gene)] # list of genes
        self.name = name
        self.alias = alias


def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Gene':
        if not 'alias' in obj:
            return Gene(species=obj['species'], name=obj['name'], alias=obj['alias'])
        else:
            return Gene(species=obj['species'], name=obj['name'], alias=obj['alias'])
    elif '__type__' in obj and obj['__type__'] == 'Transcript':
        if not 'alias' in obj:
            return Transcript(gene=obj['gene'], name=obj['name'])
        else:
            return Transcript(gene=obj['gene'], name=obj['name'], alias=obj['alias'])
    elif '__type__' in obj and  obj['__type__'] == 'Orthogroup':
        return Orthogroup(name=obj["name"], genes=obj["members"])
    return obj

with open(os.sep.join([os.path.abspath(os.path.dirname(__file__)),"gene_data.json"]), mode='r', encoding="utf-8") as data_file:
    genelist = json.loads(data_file.read(), object_hook=object_decoder)
    for g in genelist:
        print(g.species, g.name, g.alias)

with open(os.sep.join([os.path.abspath(os.path.dirname(__file__)),"transcript_data.json"]), mode='r', encoding="utf-8") as data_file:
    transcriptlist= json.loads(data_file.read(), object_hook=object_decoder)
    for t in transcriptlist:
        print(t.gene, t.name, t.alias)


with open(os.sep.join([os.path.abspath(os.path.dirname(__file__)),"orthogroup_data.json"]), mode='r', encoding="utf-8") as data_file:
    orthogrouplist= json.loads(data_file.read(), object_hook=object_decoder)
    for t in orthogrouplist:
        print([x.name for x in t.genes], t.name, t.alias)
