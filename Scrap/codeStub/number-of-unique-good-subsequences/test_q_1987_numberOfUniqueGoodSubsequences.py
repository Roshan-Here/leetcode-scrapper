import pytest
from q_1987_numberOfUniqueGoodSubsequences import Solution


@pytest.mark.parametrize("binary, output", [("001", 2), ("11", 2), ("101", 5)])
class TestSolution:
    def test_numberOfUniqueGoodSubsequences(self, binary: str, output: int):
        sc = Solution()
        assert (
            sc.numberOfUniqueGoodSubsequences(
                binary,
            )
            == output
        )
