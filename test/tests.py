from typing import Any
import astroid
import src.variable_declaration_checker
import pylint.testutils


class Tests(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = src.variable_declaration_checker.VariableDeclarationChecker

    def test_1(self):
        self.checker: Tests.CHECKER_CLASS

        f1, f2 = astroid.extract_node(
            """
            x1: int = 1
            def f1(): #@
                x2: int = 2
                def f2(): #@
                    global x1
                    nonlocal x2
                    x1 = 1
                    x2 = 2
            """)
        with self.assertNoMessages():
            self.checker.visit_functiondef(f1)
            self.checker.visit_functiondef(f2)

    def test_2(self):
        self.checker: Tests.CHECKER_CLASS

        module: Any = astroid.parse(
            """
            x1: int = 1
            def f1():
                x2: int = 2
                def f2():
                    global x1
                    nonlocal x2
                    x1: int = 1
                    x2: int = 2
            """)
        f1 = module.locals["f1"][0]
        f2 = f1.locals["f2"][0]
        f2x1 = f2.body[2].target
        f2x2 = f2.body[3].target

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="re-declared-variable",
                node=f2x1,
                line=f2x1.lineno,
                end_line=f2x1.end_lineno,
                col_offset=f2x1.col_offset,
                end_col_offset=f2x1.end_col_offset
            ),):
            self.checker.visit_module(module)

        with self.assertNoMessages():
            self.checker.visit_functiondef(f1)

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="re-declared-variable",
                node=f2x2,
                line=f2x2.lineno,
                end_line=f2x2.end_lineno,
                col_offset=f2x2.col_offset,
                end_col_offset=f2x2.end_col_offset
            ),):
            self.checker.visit_functiondef(f2)
