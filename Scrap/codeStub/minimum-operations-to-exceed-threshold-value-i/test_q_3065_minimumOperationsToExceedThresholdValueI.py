import pytest
from q_3065_minimumOperationsToExceedThresholdValueI import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([2, 11, 10, 1, 3], 10, 3), ([1, 1, 2, 4, 9], 1, 0), ([1, 1, 2, 4, 9], 9, 4)],
)
class TestSolution:
    def test_minOperations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                k,
            )
            == output
        )
