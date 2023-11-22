import gpt_4_search as backend
import sys
from os import devnull

inp = sys.argv[1] if len(sys.argv) > 1 else input("> ")
try:
    backend.FEVER = [True]
    if len(sys.argv) == 4:
        backend.FEVER = sys.argv[2:]
    sys.stdout = open(devnull, 'w')
    output = backend.run(inp)
    sys.stdout = sys.__stdout__
    print(output)
    if backend.references:
        print("\n**References:**")
    backend.show_references()
except Exception as e:
    print(f"`Error: {str(e)}`")