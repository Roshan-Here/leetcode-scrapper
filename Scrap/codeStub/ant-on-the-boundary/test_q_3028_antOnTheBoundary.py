import pytest
from q_3028_antOnTheBoundary import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, -5], 1), ([3, 2, -3, -4], 0)])
class TestSolution:
    def test_returnToBoundaryCount(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.returnToBoundaryCount(
                nums,
            )
            == output
        )
