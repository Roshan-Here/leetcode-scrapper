import pytest
from q_1551_minimumOperationsToMakeArrayEqual import Solution


@pytest.mark.parametrize("n, output", [(3, 2), (6, 9)])
class TestSolution:
    def test_minOperations(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                n,
            )
            == output
        )
