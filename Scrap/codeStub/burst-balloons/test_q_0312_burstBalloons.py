import pytest
from q_0312_burstBalloons import Solution


@pytest.mark.parametrize("nums, output", [([3, 1, 5, 8], 167), ([1, 5], 10)])
class TestSolution:
    def test_maxCoins(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxCoins(
                nums,
            )
            == output
        )
