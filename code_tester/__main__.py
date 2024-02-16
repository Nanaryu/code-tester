import os
import time

from . import cli
from .process import get_proc_output

TESTS_DIR = "tests"
COMMAND_FILE = "test_cmd.txt"


class TestCase:
    def __init__(
        self, command: str, input_data: str, expected_output_data: str
    ) -> None:
        self.command = command.strip()
        self.input_data = input_data.replace("\r\n", "\n").rstrip()
        self.expected_output_data = expected_output_data.replace("\r\n", "\n").rstrip()

    def run_test(self) -> tuple[str, str]:
        input_data = self.input_data.encode()
        output_data, error_data = get_proc_output(self.command, input_data)
        output_data = output_data.decode().replace("\r\n", "\n").rstrip()
        error_data = error_data.decode().replace("\r\n", "\n").rstrip()
        return output_data, error_data


def get_test_cases(tests_dir: str, command_file: str) -> list[TestCase]:
    test_cases: list[TestCase] = []

    with open(command_file, "r") as f:
        test_command = f.readline()

    test_count = 0
    while True:
        test_in_file = os.path.join(tests_dir, f"{test_count+1}.in")
        test_out_file = os.path.join(tests_dir, f"{test_count+1}.out")
        if not os.path.isfile(test_in_file) or not os.path.isfile(test_out_file):
            break
        test_count += 1

        with open(test_in_file, "r") as f:
            input_data = f.read()

        with open(test_out_file, "r") as f:
            expected_output_data = f.read()

        test_cases.append(TestCase(test_command, input_data, expected_output_data))

    return test_cases


def main() -> None:
    cli.init_color()
    cli.clear_console()

    test_cases = get_test_cases(TESTS_DIR, COMMAND_FILE)

    if not test_cases:
        cli.clear_console()
        print("NO TESTS FOUND")
        time.sleep(1)

    for test_case in test_cases:
        print(test_case)


if __name__ == "__main__":
    main()
