# Supplied checks for your program.
#
# Run from this folder:
#
#     python3 test.py -v
#
# (On Windows use: py -3 test.py -v)
#
# This file runs the following checks against Pattern.py:
#
# 1. The six given functions are still there with their names and parameters
#    unchanged, and no other functions are defined.
# 2. count_filled, fill_carpet and fill_tromino call themselves (recursion),
#    main() calls count_filled, fill_carpet, fill_tromino and print_grid, and
#    fill_tromino calls find_quadrant, as in the table in brief.md.
# 3. Direct checks of fill_carpet, fill_tromino and print_grid on small grids,
#    including regions that do not start at (0, 0).
# 4. The five worked examples from brief.md and the level-0 cases, as
#    whole-program runs.
# 5. Your own tests in tests.txt: every function check under "# Function
#    checks" and every program case under "# Program cases".
#
# Passing these checks is not your test mark. Designing your own tests in
# tests.txt is a separate, graded part of the assignment: see "Testing your
# program" in brief.md. Work out every expected value by hand before you run
# anything. A test of yours that fails may mean your program is wrong, or that
# your expected value is wrong. Find out which.
#
# What you should see:
#
# - ALL checks passing ends with:
#
#       ----------------------------------------------------------------------
#       Ran N tests in ...s
#
#       OK
#
# - If SOME checks fail, each failed one is listed under "FAIL:" with what
#   your program gave and what was expected; the run ends with
#   "FAILED (failures=N)". With the untouched template the output checks fail,
#   because the functions return None and main() prints nothing.
#
# Fix the first failing check and re-run; repeat until you get "OK".
#
# Do not change this file.

import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROGRAM = HERE / "Pattern.py"
TESTS_FILE = HERE / "tests.txt"

TIMEOUT = 30

GIVEN_FUNCTIONS = {
    "count_filled": ["level"],
    "fill_carpet": ["grid", "top", "left", "size"],
    "find_quadrant": ["top", "left", "size", "row", "col"],
    "fill_tromino": ["grid", "top", "left", "size", "hole_row", "hole_col", "tile"],
    "print_grid": ["grid"],
    "main": [],
}
CHECKABLE = ["count_filled", "find_quadrant"]
RECURSIVE = ["count_filled", "fill_carpet", "fill_tromino"]
REQUIRED_CALLS = {
    "main": ["count_filled", "fill_carpet", "fill_tromino", "print_grid"],
    "fill_tromino": ["find_quadrant"],
}

PROMPTS = [
    "Pattern (1 carpet, 2 tromino): ",
    "Hole column: ",
    "Hole row: ",
    "Level: ",
]

MAX_FUNCTION_CHECKS = 12
MAX_PROGRAM_CASES = 8


# ---- The worked examples from brief.md ----

# Rows of the level-2 carpet (Example 1). The level-3 carpet (Example 2) is
# built from them: three copies side by side, or two copies with an empty
# middle.
A9 = "  #" * 9
B9 = "  #  .  #" * 3
C9 = "  #  #  #  .  .  .  #  #  #"
D9 = "  #  .  #  .  .  .  #  .  #"
E9 = "  ." * 9
LEVEL_2_ROWS = [A9, B9, A9, C9, D9, C9, A9, B9, A9]

EXAMPLE_1_INPUT = "1\n2\n"
EXAMPLE_1_OUTPUT = LEVEL_2_ROWS + ["Filled: 64"]

EXAMPLE_2_INPUT = "1\n3\n"
EXAMPLE_2_OUTPUT = (
    [row * 3 for row in LEVEL_2_ROWS]
    + [row + E9 + row for row in LEVEL_2_ROWS]
    + [row * 3 for row in LEVEL_2_ROWS]
    + ["Filled: 512"]
)

EXAMPLE_3_INPUT = "2\n2\n0\n0\n"
EXAMPLE_3_OUTPUT = [
    "  X  2  3  3",
    "  2  2  1  3",
    "  4  1  1  5",
    "  4  4  5  5",
    "Tiles: 5",
]

EXAMPLE_4_INPUT = "2\n2\n1\n2\n"
EXAMPLE_4_OUTPUT = [
    "  2  2  3  3",
    "  2  1  X  3",
    "  4  1  1  5",
    "  4  4  5  5",
    "Tiles: 5",
]

EXAMPLE_5_INPUT = "2\n4\n5\n10\n"
EXAMPLE_5_OUTPUT = [
    "  4  4  5  5  9  9 10 10 25 25 26 26 30 30 31 31",
    "  4  3  3  5  9  8  8 10 25 24 24 26 30 29 29 31",
    "  6  3  7  7 11 11  8 12 27 24 28 28 32 32 29 33",
    "  6  6  7  2  2 11 12 12 27 27 28 23 23 32 33 33",
    " 14 14 15  2 19 19 20 20 35 35 36 36 23 40 41 41",
    " 14 13 15 15 19 18 18 20 35 34  X 36 40 40 39 41",
    " 16 13 13 17 21 18 22 22 37 34 34 38 42 39 39 43",
    " 16 16 17 17 21 21 22  1 37 37 38 38 42 42 43 43",
    " 46 46 47 47 51 51 52  1  1 67 68 68 72 72 73 73",
    " 46 45 45 47 51 50 52 52 67 67 66 68 72 71 71 73",
    " 48 45 49 49 53 50 50 54 69 66 66 70 74 74 71 75",
    " 48 48 49 44 53 53 54 54 69 69 70 70 65 74 75 75",
    " 56 56 57 44 44 61 62 62 77 77 78 65 65 82 83 83",
    " 56 55 57 57 61 61 60 62 77 76 78 78 82 82 81 83",
    " 58 55 55 59 63 60 60 64 79 76 76 80 84 81 81 85",
    " 58 58 59 59 63 63 64 64 79 79 80 80 84 84 85 85",
    "Tiles: 85",
]


# ---- Running the program ----

def run_program(stdin_text):
    """Run Pattern.py with the given input. Return (printed lines, error text)."""
    result = subprocess.run(
        [sys.executable, str(PROGRAM)],
        input=stdin_text,
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
    )
    if result.returncode != 0:
        return None, result.stderr
    printed = result.stdout
    for prompt in PROMPTS:
        printed = printed.replace(prompt, "")
    return printed.splitlines(), None


# Calling one function. Pattern.py ends with main(), which reads input, so the
# function is called from a copy of Pattern.py with that last call left out.
FUNCTION_RUNNER = r"""
import ast, contextlib, io, json, sys
path, name, args_json = sys.argv[1], sys.argv[2], sys.argv[3]
source = open(path, encoding="utf-8").read()
tree = ast.parse(source, filename=path)
tree.body = [
    node for node in tree.body
    if not (isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "main")
]
namespace = {"__name__": "pattern_under_test"}
exec(compile(tree, path, "exec"), namespace)
args = json.loads(args_json)
output = io.StringIO()
with contextlib.redirect_stdout(output):
    value = namespace[name](*args)
if isinstance(value, (bool, int, float, type(None))):
    answer = {"repr": repr(value), "value": value}
else:
    answer = {"repr": repr(value), "value": None, "odd": True}
answer["stdout"] = output.getvalue()
answer["args_after"] = args
print(json.dumps(answer))
"""


def run_function(name, args):
    """Call one function in Pattern.py. Return (answer dict, error text)."""
    result = subprocess.run(
        [sys.executable, "-c", FUNCTION_RUNNER, str(PROGRAM), name, json.dumps(args)],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
    )
    if result.returncode != 0:
        return None, result.stderr
    lines = result.stdout.strip().splitlines()
    if not lines:
        return None, "the call printed nothing back"
    try:
        return json.loads(lines[-1]), None
    except ValueError:
        return None, "could not read the result:\n" + result.stdout


def call_function(name, args):
    """Return (value, repr, error) for a function check."""
    answer, error = run_function(name, args)
    if error is not None:
        return None, None, error
    if answer.get("odd"):
        return object(), answer["repr"], None
    return answer["value"], answer["repr"], None


# ---- Reading tests.txt ----

class TestsFileError(Exception):
    pass


def parse_function_check(line):
    try:
        tree = ast.parse(line, mode="eval")
    except SyntaxError:
        raise TestsFileError("this is not a valid Python expression")
    expr = tree.body
    if not (isinstance(expr, ast.Compare)
            and len(expr.ops) == 1
            and isinstance(expr.ops[0], ast.Eq)):
        raise TestsFileError("a function check must be a call, then ==, then the expected value")
    call = expr.left
    if not (isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id in CHECKABLE
            and not call.keywords):
        raise TestsFileError(
            "the left side must call one of " + ", ".join(CHECKABLE)
            + ", with plain values in the brackets"
        )
    try:
        args = [ast.literal_eval(arg) for arg in call.args]
        expected = ast.literal_eval(expr.comparators[0])
    except ValueError:
        raise TestsFileError("use plain numbers, True or False, not variables or sums")
    return call.func.id, args, expected


def is_int_line(text):
    text = text.strip()
    if text.startswith("-"):
        text = text[1:]
    return text.isdigit()


def parse_program_case(block):
    """Split a block of lines into (input text, expected output lines)."""
    split = 0
    while split < len(block) and is_int_line(block[split]):
        split += 1
    inputs, outputs = block[:split], block[split:]
    if not inputs:
        raise TestsFileError("the case has no input lines (one whole number per line)")
    if not outputs:
        raise TestsFileError("the case has no expected output after its input")
    pattern = inputs[0].strip()
    if pattern not in ("1", "2"):
        raise TestsFileError("the first input line must be 1 (carpet) or 2 (tromino)")
    if pattern == "1" and len(inputs) != 2:
        raise TestsFileError("a carpet case has 2 input lines: 1, then the level")
    if pattern == "2" and len(inputs) != 4:
        raise TestsFileError(
            "a tromino case has 4 input lines: 2, the level, the hole row, the hole column"
        )
    outputs = [line.rstrip() for line in outputs]
    last = outputs[-1]
    if not (last.startswith("Filled: ") or last.startswith("Tiles: ")):
        raise TestsFileError("the last line of a case must be the summary line (Filled: ... or Tiles: ...)")
    for line in outputs[:-1]:
        if not line.startswith(" "):
            raise TestsFileError(
                "every grid line starts with spaces, because each cell takes three "
                "characters. Did your editor remove the spaces at the start of a line?"
            )
    return "\n".join(line.strip() for line in inputs) + "\n", outputs


def read_tests_file():
    if not TESTS_FILE.exists():
        return [], [], [(0, "tests.txt not found next to test.py")]
    lines = TESTS_FILE.read_text(encoding="utf-8").splitlines()
    section = None
    checks, cases, problems = [], [], []
    block, block_start = [], 0

    def close_block():
        if block:
            try:
                cases.append((block_start, parse_program_case(block)))
            except TestsFileError as error:
                problems.append((block_start, str(error)))

    for number, raw in enumerate(lines, start=1):
        line = raw.strip()
        if line.lower() == "# function checks":
            close_block()
            block = []
            section = "functions"
            continue
        if line.lower() == "# program cases":
            close_block()
            block = []
            section = "programs"
            continue
        if section == "functions":
            if not line or raw.startswith("#"):
                continue
            try:
                checks.append((number, line, parse_function_check(line)))
            except TestsFileError as error:
                problems.append((number, str(error)))
        elif section == "programs":
            if not line:
                close_block()
                block = []
                continue
            if not block:
                block_start = number
            block.append(raw)
        elif line:
            problems.append((number, "this line is above both section headings"))
    close_block()
    if section is None:
        problems.append((0, 'tests.txt needs the lines "# Function checks" and "# Program cases"'))
    return checks, cases, problems


# ---- The checks ----

def read_tree(test):
    if not PROGRAM.exists():
        test.fail(f"Pattern.py not found next to test.py (looked at {PROGRAM})")
    try:
        return ast.parse(PROGRAM.read_text(encoding="utf-8"))
    except SyntaxError as error:
        test.fail(f"Pattern.py is not valid Python: {error}")


def calls_function(node, name):
    """True if anywhere inside node there is a call to name(...)."""
    return any(
        isinstance(inner, ast.Call)
        and isinstance(inner.func, ast.Name)
        and inner.func.id == name
        for inner in ast.walk(node)
    )


class GivenFunctionTests(unittest.TestCase):
    def test_given_functions_unchanged(self):
        tree = read_tree(self)
        definitions = [
            node for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        self.assertEqual(
            len(definitions), len(GIVEN_FUNCTIONS),
            "Define only the six supplied functions. Do not add helper functions, "
            "nested functions or duplicate definitions",
        )
        found = {
            node.name: [arg.arg for arg in node.args.args]
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
        }
        for name, params in GIVEN_FUNCTIONS.items():
            with self.subTest(function=name):
                self.assertIn(name, found, f"{name}() is missing from Pattern.py. Do not rename the given functions")
                self.assertEqual(
                    found[name], params,
                    f"{name}() must keep its parameters exactly: {name}({', '.join(params)})",
                )

    def test_recursive_functions_call_themselves(self):
        tree = read_tree(self)
        defs = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
        for name in RECURSIVE:
            with self.subTest(function=name):
                self.assertIn(name, defs, f"{name}() is missing from Pattern.py")
                self.assertTrue(
                    calls_function(defs[name], name),
                    f"{name}() must be recursive: its body must call {name}()",
                )

    def test_functions_used_as_in_brief(self):
        tree = read_tree(self)
        defs = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
        for caller, callees in REQUIRED_CALLS.items():
            for callee in callees:
                with self.subTest(caller=caller, callee=callee):
                    self.assertIn(caller, defs, f"{caller}() is missing from Pattern.py")
                    self.assertTrue(
                        calls_function(defs[caller], callee),
                        f"{caller}() must call {callee}(): see the 'Used by' column in brief.md",
                    )


class DirectFunctionTests(unittest.TestCase):
    def call(self, name, args):
        answer, error = run_function(name, args)
        if answer is None:
            self.fail(f"{name}() crashed:\n{error}")
        return answer

    # print_grid

    def test_print_grid_single_cell(self):
        grid = [["#"]]
        answer = self.call("print_grid", [grid])
        self.assertEqual(answer["stdout"], "  #\n")
        self.assertEqual(answer["repr"], "None", "print_grid must return nothing")
        self.assertEqual(answer["args_after"], [grid], "print_grid must not change the grid")

    def test_print_grid_strings_and_numbers(self):
        grid = [["X", 1], [12, 1]]
        answer = self.call("print_grid", [grid])
        self.assertEqual(answer["stdout"], "  X  1\n 12  1\n",
                         "each cell must take exactly three characters")
        self.assertEqual(answer["args_after"], [grid], "print_grid must not change the grid")

    # fill_carpet

    def test_fill_carpet_whole_grid(self):
        grid = [["."] * 3 for _ in range(3)]
        answer = self.call("fill_carpet", [grid, 0, 0, 3])
        self.assertEqual(answer["repr"], "None", "fill_carpet must return nothing")
        self.assertEqual(answer["stdout"], "", "fill_carpet must not print")
        self.assertEqual(answer["args_after"][0],
                         [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]])

    def test_fill_carpet_leaves_empty_cells_unchanged(self):
        grid = [["?"] * 3 for _ in range(3)]
        answer = self.call("fill_carpet", [grid, 0, 0, 3])
        self.assertEqual(answer["args_after"][0],
                         [["#", "#", "#"], ["#", "?", "#"], ["#", "#", "#"]],
                         "fill_carpet must only set filled cells to '#', and not change empty cells")

    def test_fill_carpet_offset_region(self):
        grid = [["."] * 6 for _ in range(3)]
        answer = self.call("fill_carpet", [grid, 0, 3, 3])
        self.assertEqual(answer["args_after"][0], [
            [".", ".", ".", "#", "#", "#"],
            [".", ".", ".", "#", ".", "#"],
            [".", ".", ".", "#", "#", "#"],
        ], "fill_carpet must draw only inside the region starting at (top, left)")

    def test_fill_carpet_single_cell(self):
        grid = [["."] * 3 for _ in range(3)]
        answer = self.call("fill_carpet", [grid, 1, 2, 1])
        self.assertEqual(answer["args_after"][0],
                         [[".", ".", "."], [".", ".", "#"], [".", ".", "."]])

    # fill_tromino

    def test_fill_tromino_base_case(self):
        grid = [["X"]]
        answer = self.call("fill_tromino", [grid, 0, 0, 1, 0, 0, 4])
        self.assertEqual(answer["repr"], "4",
                         "a region of side 1 places nothing, so the next unused number is still tile")
        self.assertEqual(answer["args_after"][0], [["X"]])

    def test_fill_tromino_two_by_two(self):
        grid = [[0, 0], [0, "X"]]
        answer = self.call("fill_tromino", [grid, 0, 0, 2, 1, 1, 1])
        self.assertEqual(answer["repr"], "2", "fill_tromino must return the next unused tile number")
        self.assertEqual(answer["stdout"], "", "fill_tromino must not print")
        self.assertEqual(answer["args_after"][0], [[1, 1], [1, "X"]])

    def test_fill_tromino_offset_region_and_start_number(self):
        grid = [[0, 0, 0, "X"], [0, 0, 0, 0]]
        answer = self.call("fill_tromino", [grid, 0, 2, 2, 0, 3, 7])
        self.assertEqual(answer["repr"], "8", "fill_tromino must return the next unused tile number")
        self.assertEqual(answer["args_after"][0], [[0, 0, 7, "X"], [0, 0, 7, 7]],
                         "fill_tromino must tile only inside its region, starting from tile")

    def test_fill_tromino_four_by_four_start_number(self):
        # Example 3, but numbering from 10 instead of 1.
        grid = [["X", 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        answer = self.call("fill_tromino", [grid, 0, 0, 4, 0, 0, 10])
        self.assertEqual(answer["repr"], "15", "fill_tromino must return the next unused tile number")
        self.assertEqual(answer["args_after"][0], [
            ["X", 11, 12, 12],
            [11, 11, 10, 12],
            [13, 10, 10, 14],
            [13, 13, 14, 14],
        ], "the center tromino gets tile, then quadrants 0, 1, 2, 3 continue the numbering")


class WorkedExampleTests(unittest.TestCase):
    def check(self, stdin_text, expected_lines):
        if not PROGRAM.exists():
            self.fail(f"Pattern.py not found next to test.py (looked at {PROGRAM})")
        printed, error = run_program(stdin_text)
        if printed is None:
            self.fail("Pattern.py crashed before finishing.\nstderr was:\n" + error)
        if not printed:
            self.fail("Pattern.py printed nothing. Is main() still empty?")
        self.assertEqual(
            printed, expected_lines,
            "Output did not match exactly (spaces, symbols, numbers and line order count)",
        )

    def test_example_1_carpet_level_2(self):
        self.check(EXAMPLE_1_INPUT, EXAMPLE_1_OUTPUT)

    def test_example_2_carpet_level_3(self):
        self.check(EXAMPLE_2_INPUT, EXAMPLE_2_OUTPUT)

    def test_example_3_tromino_hole_in_corner(self):
        self.check(EXAMPLE_3_INPUT, EXAMPLE_3_OUTPUT)

    def test_example_4_tromino_hole_on_center_cell(self):
        self.check(EXAMPLE_4_INPUT, EXAMPLE_4_OUTPUT)

    def test_example_5_tromino_level_4(self):
        self.check(EXAMPLE_5_INPUT, EXAMPLE_5_OUTPUT)

    def test_carpet_level_0(self):
        self.check("1\n0\n", ["  #", "Filled: 1"])

    def test_tromino_level_0(self):
        self.check("2\n0\n0\n0\n", ["  X", "Tiles: 0"])


class YourTestsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checks, cls.cases, cls.problems = read_tests_file()

    def test_tests_file_layout(self):
        for line_number, message in self.problems:
            where = f"line {line_number}" if line_number else "tests.txt"
            with self.subTest(where=where):
                self.fail(f"tests.txt, {where}: {message}")
        if len(self.checks) > MAX_FUNCTION_CHECKS:
            self.fail(f"tests.txt has {len(self.checks)} function checks; "
                      f"the brief allows up to {MAX_FUNCTION_CHECKS}")
        if len(self.cases) > MAX_PROGRAM_CASES:
            self.fail(f"tests.txt has {len(self.cases)} program cases; "
                      f"the brief allows up to {MAX_PROGRAM_CASES}")

    def test_your_function_checks(self):
        if not self.checks:
            self.skipTest("no function checks in tests.txt yet")
        for line_number, text, (name, args, expected) in self.checks:
            with self.subTest(line=line_number, check=text):
                value, shown, error = call_function(name, args)
                if error is not None:
                    self.fail(f"tests.txt line {line_number}: {text}\n{name}() crashed:\n{error}")
                if not value == expected:
                    self.fail(f"tests.txt line {line_number}: {text}\n"
                              f"{name}() returned {shown}, you expected {expected!r}")

    def test_your_program_cases(self):
        if not self.cases:
            self.skipTest("no program cases in tests.txt yet")
        for line_number, (stdin_text, expected_lines) in self.cases:
            with self.subTest(case_starting_at_line=line_number):
                printed, error = run_program(stdin_text)
                if printed is None:
                    self.fail(f"tests.txt case at line {line_number}: Pattern.py crashed.\n"
                              f"stderr was:\n{error}")
                self.assertEqual(printed, expected_lines,
                                 f"tests.txt case at line {line_number}: "
                                 f"output did not match your expected output")


if __name__ == "__main__":
    unittest.main()
