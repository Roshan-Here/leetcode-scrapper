import pytest
from q_0131_palindromePartitioning import Solution


@pytest.mark.parametrize(
    "s, output", [("aab", [["a", "a", "b"], ["aa", "b"]]), ("a", [["a"]])]
)
class TestSolution:
    def test_partition(self, s: str, output: List[List[str]]):
        sc = Solution()
        assert (
            sc.partition(
                s,
            )
            == output
        )
