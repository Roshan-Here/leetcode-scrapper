import pytest
from q_2919_minimumIncrementOperationsToMakeArrayBeautiful import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([2, 3, 0, 0, 2], 4, 3), ([0, 1, 3, 3], 5, 2), ([1, 1, 2], 1, 0)],
)
class TestSolution:
    def test_minIncrementOperations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minIncrementOperations(
                nums,
                k,
            )
            == output
        )
