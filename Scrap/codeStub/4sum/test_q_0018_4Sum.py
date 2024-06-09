import pytest
from q_0018_4Sum import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ],
)
class TestSolution:
    def test_fourSum(self, nums: List[int], target: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.fourSum(
                nums,
                target,
            )
            == output
        )
