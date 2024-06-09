import pytest
from q_1092_shortestCommonSupersequence import Solution


@pytest.mark.parametrize(
    "str1, str2, output",
    [("abac", "cab", "cabac"), ("aaaaaaaa", "aaaaaaaa", "aaaaaaaa")],
)
class TestSolution:
    def test_shortestCommonSupersequence(self, str1: str, str2: str, output: str):
        sc = Solution()
        assert (
            sc.shortestCommonSupersequence(
                str1,
                str2,
            )
            == output
        )
