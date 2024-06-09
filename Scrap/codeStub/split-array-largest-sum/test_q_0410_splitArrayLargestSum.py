import pytest
from q_0410_splitArrayLargestSum import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([7, 2, 5, 10, 8], 2, 18), ([1, 2, 3, 4, 5], 2, 9)]
)
class TestSolution:
    def test_splitArray(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.splitArray(
                nums,
                k,
            )
            == output
        )
