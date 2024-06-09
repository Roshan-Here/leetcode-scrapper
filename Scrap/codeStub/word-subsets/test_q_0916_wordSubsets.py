import pytest
from q_0916_wordSubsets import Solution


@pytest.mark.parametrize(
    "words1, words2, output",
    [
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "o"],
            ["facebook", "google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["l", "e"],
            ["apple", "google", "leetcode"],
        ),
    ],
)
class TestSolution:
    def test_wordSubsets(self, words1: List[str], words2: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.wordSubsets(
                words1,
                words2,
            )
            == output
        )
