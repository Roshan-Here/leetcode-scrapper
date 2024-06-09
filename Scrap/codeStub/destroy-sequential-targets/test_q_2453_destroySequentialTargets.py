import pytest
from q_2453_destroySequentialTargets import Solution


@pytest.mark.parametrize(
    "nums, space, output",
    [([3, 7, 8, 1, 1, 5], 2, 1), ([1, 3, 5, 2, 4, 6], 2, 1), ([6, 2, 5], 100, 2)],
)
class TestSolution:
    def test_destroyTargets(self, nums: List[int], space: int, output: int):
        sc = Solution()
        assert (
            sc.destroyTargets(
                nums,
                space,
            )
            == output
        )
