import pytest
from q_0016_3SumClosest import Solution


@pytest.mark.parametrize(
    "nums, target, output", [([-1, 2, 1, -4], 1, 2), ([0, 0, 0], 1, 0)]
)
class TestSolution:
    def test_threeSumClosest(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.threeSumClosest(
                nums,
                target,
            )
            == output
        )
