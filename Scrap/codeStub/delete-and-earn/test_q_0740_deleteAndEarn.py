import pytest
from q_0740_deleteAndEarn import Solution


@pytest.mark.parametrize("nums, output", [([3, 4, 2], 6), ([2, 2, 3, 3, 3, 4], 9)])
class TestSolution:
    def test_deleteAndEarn(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.deleteAndEarn(
                nums,
            )
            == output
        )
