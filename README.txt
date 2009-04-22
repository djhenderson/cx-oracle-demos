To create a demo file, make a python file with these members:

def demo():


desc="""one-liner description of demo"""

setup="""
any setup notes, e.g. CREATE TABLE.
can be empty.
"""

cleanup="""
any cleanup notes, e.g. DROP TABLE.
can be empty.
"""

notes="""
notes explaining the demo.
required.
"""

output="""
the output of the program, if useful.
"""

def demo():

    # the demo code.  no code, imports, or anything besides the
    # text strings above should appear outside the function.
    # use connect.py as a model.
