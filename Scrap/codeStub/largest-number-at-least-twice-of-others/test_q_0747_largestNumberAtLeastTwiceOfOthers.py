import pytest
from q_0747_largestNumberAtLeastTwiceOfOthers import Solution


@pytest.mark.parametrize("nums, output", [([3, 6, 1, 0], 1), ([1, 2, 3, 4], -1)])
class TestSolution:
    def test_dominantIndex(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.dominantIndex(
                nums,
            )
            == output
        )
