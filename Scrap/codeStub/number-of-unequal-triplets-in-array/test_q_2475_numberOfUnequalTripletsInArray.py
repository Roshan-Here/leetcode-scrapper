import pytest
from q_2475_numberOfUnequalTripletsInArray import Solution


@pytest.mark.parametrize("nums, output", [([4, 4, 2, 4, 3], 3), ([1, 1, 1, 1, 1], 0)])
class TestSolution:
    def test_unequalTriplets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.unequalTriplets(
                nums,
            )
            == output
        )
