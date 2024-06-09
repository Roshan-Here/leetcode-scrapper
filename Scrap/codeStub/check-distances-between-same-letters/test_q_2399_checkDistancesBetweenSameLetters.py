import pytest
from q_2399_checkDistancesBetweenSameLetters import Solution


@pytest.mark.parametrize(
    "s, distance, output",
    [
        (
            "abaccb",
            [
                1,
                3,
                0,
                5,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            True,
        ),
        (
            "aa",
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            False,
        ),
    ],
)
class TestSolution:
    def test_checkDistances(self, s: str, distance: List[int], output: bool):
        sc = Solution()
        assert (
            sc.checkDistances(
                s,
                distance,
            )
            == output
        )
