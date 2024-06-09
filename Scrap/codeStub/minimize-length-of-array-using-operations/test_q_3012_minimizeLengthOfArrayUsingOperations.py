import pytest
from q_3012_minimizeLengthOfArrayUsingOperations import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 4, 3, 1], 1), ([5, 5, 5, 10, 5], 2), ([2, 3, 4], 1)]
)
class TestSolution:
    def test_minimumArrayLength(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumArrayLength(
                nums,
            )
            == output
        )
