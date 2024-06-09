import pytest
from q_1296_divideArrayInSetsOfKConsecutiveNumbers import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 2, 3, 3, 4, 4, 5, 6], 4, True),
        ([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3, True),
        ([1, 2, 3, 4], 3, False),
    ],
)
class TestSolution:
    def test_isPossibleDivide(self, nums: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.isPossibleDivide(
                nums,
                k,
            )
            == output
        )
