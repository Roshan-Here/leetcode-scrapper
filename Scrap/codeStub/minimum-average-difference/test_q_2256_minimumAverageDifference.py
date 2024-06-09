import pytest
from q_2256_minimumAverageDifference import Solution


@pytest.mark.parametrize("nums, output", [([2, 5, 3, 9, 5, 3], 3), ([0], 0)])
class TestSolution:
    def test_minimumAverageDifference(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumAverageDifference(
                nums,
            )
            == output
        )
