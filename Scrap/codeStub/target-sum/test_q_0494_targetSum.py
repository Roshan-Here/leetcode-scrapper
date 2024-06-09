import pytest
from q_0494_targetSum import Solution


@pytest.mark.parametrize("nums, target, output", [([1, 1, 1, 1, 1], 3, 5), ([1], 1, 1)])
class TestSolution:
    def test_findTargetSumWays(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.findTargetSumWays(
                nums,
                target,
            )
            == output
        )
