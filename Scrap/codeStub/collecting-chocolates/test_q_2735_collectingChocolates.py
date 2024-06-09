import pytest
from q_2735_collectingChocolates import Solution


@pytest.mark.parametrize("nums, x, output", [([20, 1, 15], 5, 13), ([1, 2, 3], 4, 6)])
class TestSolution:
    def test_minCost(self, nums: List[int], x: int, output: int):
        sc = Solution()
        assert (
            sc.minCost(
                nums,
                x,
            )
            == output
        )
