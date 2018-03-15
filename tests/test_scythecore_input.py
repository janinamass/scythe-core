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


with open(os.path.abspath(os.path.dirname(__file__))+os.sep+"data.json", encoding='utf-8') as data_file:
    data = json.loads(data_file.read())
    pprint (data)
    raise Exception
paths()