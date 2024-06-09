import pytest
from q_2789_largestElementInAnArrayAfterMergeOperations import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, 7, 9, 3], 21), ([5, 3, 3], 11)])
class TestSolution:
    def test_maxArrayValue(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxArrayValue(
                nums,
            )
            == output
        )
