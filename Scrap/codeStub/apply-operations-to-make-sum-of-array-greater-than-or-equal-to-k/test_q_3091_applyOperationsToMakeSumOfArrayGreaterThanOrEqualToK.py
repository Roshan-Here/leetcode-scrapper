import pytest
from q_3091_applyOperationsToMakeSumOfArrayGreaterThanOrEqualToK import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minOperations(self, k: int, output: int):
        sc = Solution()
        assert sc.minOperations() == output
