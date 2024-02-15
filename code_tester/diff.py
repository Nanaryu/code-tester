from dataclasses import dataclass
from enum import Enum

import diff_match_patch as dmp_module  # type: ignore

dmp = dmp_module.diff_match_patch()


class DiffType(Enum):
    KEEP = 0
    INSERT = 1
    REMOVE = -1


diff_types = {diff_type.value: diff_type for diff_type in DiffType}


@dataclass(frozen=True, slots=True)
class Diff:
    data: str
    diff_type: DiffType


def get_diff(text1: str, text2: str) -> list[Diff]:
    return [Diff(diff[1], diff_types[diff[0]]) for diff in dmp.diff_main(text1, text2)]  # type: ignore
