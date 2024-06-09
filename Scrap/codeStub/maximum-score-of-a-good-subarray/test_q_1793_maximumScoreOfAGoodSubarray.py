import pytest
from q_1793_maximumScoreOfAGoodSubarray import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 4, 3, 7, 4, 5], 3, 15), ([5, 5, 4, 5, 4, 1, 1, 1], 0, 20)]
)
class TestSolution:
    def test_maximumScore(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumScore(
                nums,
                k,
            )
            == output
        )
