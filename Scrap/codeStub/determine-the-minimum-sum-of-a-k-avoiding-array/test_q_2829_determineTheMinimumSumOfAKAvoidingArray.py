import pytest
from q_2829_determineTheMinimumSumOfAKAvoidingArray import Solution


@pytest.mark.parametrize("n, k, output", [(5, 4, 18), (2, 6, 3)])
class TestSolution:
    def test_minimumSum(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumSum(
                n,
                k,
            )
            == output
        )
