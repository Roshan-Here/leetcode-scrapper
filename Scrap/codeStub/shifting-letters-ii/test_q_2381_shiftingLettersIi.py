import pytest
from q_2381_shiftingLettersIi import Solution


@pytest.mark.parametrize(
    "s, shifts, output",
    [
        ("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]], "ace"),
        ("dztz", [[0, 0, 0], [1, 1, 1]], "catz"),
    ],
)
class TestSolution:
    def test_shiftingLetters(self, s: str, shifts: List[List[int]], output: str):
        sc = Solution()
        assert (
            sc.shiftingLetters(
                s,
                shifts,
            )
            == output
        )
