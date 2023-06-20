# Example
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--a", help="test arg A", default=5)
parser.add_argument("--b", help="test arg B", default=10)

args = parser.parse_args()

print(args)
