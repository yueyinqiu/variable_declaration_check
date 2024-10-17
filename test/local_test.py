import astroid.nodes

module = astroid.parse(
"""
x1 = 1                      # Line 1
def f1():                   # Line 2
    x2 = 2                  # Line 3
    def f2():               # Line 4
        global x1           # Line 5
        nonlocal x2         # Line 6
        x1 = 1              # Line 7
        x2 = 2              # Line 8
""")

f2 = module.locals["f1"][0].locals["f2"][0]
print(f2.locals)

# Output:
# {'x2': [<AssignName.x2 l.9 at 0x1ddffab04d0>]}
