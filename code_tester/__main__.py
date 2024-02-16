import os
import time
from datetime import datetime

from . import cli
from .color import Color
from .process import get_proc_output
from .ui import msgbox

TESTS_DIR = "tests"
COMMAND_FILE = "test_cmd.txt"


class COLORS:
    GENERAL = Color("#fff")
    TEST_PASSED = Color("#0f0")
    TEST_FAILED = Color("#f00")
    ERROR = Color("#f00")


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

    success_prev = False
    while True:
        test_cases = get_test_cases(TESTS_DIR, COMMAND_FILE)

        if not test_cases:
            cli.clear_console()
            print("NO TESTS FOUND")
            time.sleep(1)
            continue

        tests_passed = [False] * len(test_cases)

        for test_case_num, test_case in enumerate(test_cases):
            output_data, error_data = test_case.run_test()
            output_data = output_data
            error_data = error_data

            test_passed = (
                not error_data and output_data == test_case.expected_output_data
            )
            tests_passed[test_case_num] = test_passed

            cli.clear_console()
            print(
                cli.color_text(
                    f"TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                    COLORS.GENERAL,
                )
            )
            print("")

            if test_passed:
                print(
                    cli.color_text(
                        f"TEST #{test_case_num+1} PASSED", COLORS.TEST_PASSED
                    )
                )
            else:
                print(
                    cli.color_text(
                        f"TEST #{test_case_num+1} FAILED", COLORS.TEST_FAILED
                    )
                )
            print("")

            cli.print_line()
            print(test_case.input_data)
            cli.print_line()
            print(output_data)
            cli.print_line()

            if error_data:
                print("ERROR:")
                print(cli.color_text(error_data, COLORS.ERROR))
                print("")

            time.sleep(0.5)
            if not test_passed:
                time.sleep(1)

        if all(tests_passed):
            if not success_prev:
                msgbox("TESTS PASSED", "ALL TESTS PASSED")
            success_prev = True
        else:
            success_prev = False


if __name__ == "__main__":
    main()
