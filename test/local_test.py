import astroid
import astroid.nodes


p = astroid.parse(
    """
    def c1():
        print(x := 1)
    def c2():
        x = 2
    x = 3
    """)
l: astroid.nodes.AnnAssign = p.body[0].locals
l.optional_assign
pass