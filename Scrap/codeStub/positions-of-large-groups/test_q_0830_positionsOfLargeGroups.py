import pytest
from q_0830_positionsOfLargeGroups import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("abbxxxxzzy", [[3, 6]]),
        ("abc", []),
        ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
    ],
)
class TestSolution:
    def test_largeGroupPositions(self, s: str, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.largeGroupPositions(
                s,
            )
            == output
        )
