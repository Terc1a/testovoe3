import pprint
import os, os.path
from pypred import Predicate

DOC = {
    "country": "Russia",
    "city": "Moscow",
    "nedostavki": ["не отдал", "не привёз","не довез", "не довёз", "не везёт", "заказ не доехал", "заказ потерян"],
}
def test_samples():
    p = os.path.dirname(os.path.abspath(__file__))
    fh = open(os.path.join(p, "doc.txt"))
    for line, pred in enumerate(fh):
        pred = pred.strip()
        obj = Predicate(pred)
        if not obj.is_valid():
            print("Invalid Predicate!")
            print("Line: ", line)
            print("Predicate: ", pred)
            info = obj.errors()
            print("Errors: ", "\n".join(info["errors"]))
            for k, v in info["regex"].iteritems():
                print("\t%s : %s" % (k, repr(v)))
            assert False
        if obj.is_valid():
            print('pass')

