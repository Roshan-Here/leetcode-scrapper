import pytest
from q_0821_shortestDistanceToACharacter import Solution


@pytest.mark.parametrize(
    "s, c, output",
    [
        ("loveleetcode", "e", [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        ("aaab", "b", [3, 2, 1, 0]),
    ],
)
class TestSolution:
    def test_shortestToChar(self, s: str, c: str, output: List[int]):
        sc = Solution()
        assert (
            sc.shortestToChar(
                s,
                c,
            )
            == output
        )
