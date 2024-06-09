import pytest
from q_2515_shortestDistanceToTargetStringInACircularArray import Solution


@pytest.mark.parametrize(
    "words, target, startIndex, output",
    [
        (["hello", "i", "am", "leetcode", "hello"], "hello", 1, 1),
        (["a", "b", "leetcode"], "leetcode", 0, 1),
        (["i", "eat", "leetcode"], "ate", 0, -1),
    ],
)
class TestSolution:
    def test_closetTarget(
        self, words: List[str], target: str, startIndex: int, output: int
    ):
        sc = Solution()
        assert (
            sc.closetTarget(
                words,
                target,
                startIndex,
            )
            == output
        )
