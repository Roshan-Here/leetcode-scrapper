import pytest
from q_2537_countTheNumberOfGoodSubarrays import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 1, 1, 1, 1], 10, 1), ([3, 1, 4, 3, 2, 2, 4], 2, 4)]
)
class TestSolution:
    def test_countGood(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countGood(
                nums,
                k,
            )
            == output
        )
