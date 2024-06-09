import pytest
from q_0220_containsDuplicateIii import Solution


@pytest.mark.parametrize(
    "nums, indexDiff, valueDiff, output",
    [([1, 2, 3, 1], 3, 0, True), ([1, 5, 9, 1, 5, 9], 2, 3, False)],
)
class TestSolution:
    def test_containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int, output: bool
    ):
        sc = Solution()
        assert (
            sc.containsNearbyAlmostDuplicate(
                nums,
                indexDiff,
                valueDiff,
            )
            == output
        )
