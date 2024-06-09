import pytest
from q_1814_countNicePairsInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([42, 11, 1, 97], 2), ([13, 10, 35, 24, 76], 4)]
)
class TestSolution:
    def test_countNicePairs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countNicePairs(
                nums,
            )
            == output
        )
