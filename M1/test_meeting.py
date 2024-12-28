import os
import pytest

from meeting import solve


INPUT_PREFIX = "input"
OUTPUT_PREFIX = "output"
TESTCASE_DIR = "testcases"

dir_path = os.path.dirname(os.path.realpath(__file__))
test_path = os.path.join(dir_path, TESTCASE_DIR)
input_files = sorted([f for f in os.listdir(test_path) if f.startswith(INPUT_PREFIX)])
files = []
for i in input_files:
    o = OUTPUT_PREFIX + i[len(INPUT_PREFIX):]
    full_input_path = os.path.join(test_path, i)
    full_output_path = os.path.join(test_path, o)
    if os.path.isfile(full_output_path):
        files.append((full_input_path, full_output_path))

# NUM_TESTS = 20
# files = [(f"testcases/input{i:02d}.txt", f"testcases/output{i:02d}.txt") for i in range(1, NUM_TESTS + 1)]
input_files = list(map(lambda x: x[0], files))  # Used as ids for the tests.


def read_input(file):
    with open(file) as f:
        n = int(f.readline())
        houses = [tuple([int(i) for i in line.split()]) for line in f]
        return n, houses

def read_output(file):
    with open(file) as f:
        return int(f.readline())


# Defines the setup of the test below. Since `params` is set to a list, this will
# execute any related tests once per item in that list (a pair of files).
# Note: The time it takes to run the fixture does not count towards the execution
# timeout. (I've checked.)
@pytest.fixture(params=files, ids=input_files)
def file_io(request):
    (input_file, output_file) = request.param
    n, houses = read_input(input_file)
    expected_total_distance = read_output(output_file)

    return n, houses, expected_total_distance


@pytest.mark.execution_timeout(2)
def test_solve(file_io):
    n, houses, expected_total_distance = file_io
    total_distance = solve(n, houses)

    assert total_distance == expected_total_distance
