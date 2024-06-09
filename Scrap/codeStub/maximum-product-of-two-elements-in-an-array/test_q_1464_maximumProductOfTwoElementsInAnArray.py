import pytest
from q_1464_maximumProductOfTwoElementsInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 4, 5, 2], 12), ([1, 5, 4, 5], 16), ([3, 7], 12)]
)
class TestSolution:
    def test_maxProduct(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxProduct(
                nums,
            )
            == output
        )
