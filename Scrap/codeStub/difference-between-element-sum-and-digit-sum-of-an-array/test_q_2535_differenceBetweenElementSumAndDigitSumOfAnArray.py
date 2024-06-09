import pytest
from q_2535_differenceBetweenElementSumAndDigitSumOfAnArray import Solution


@pytest.mark.parametrize("nums, output", [([1, 15, 6, 3], 9), ([1, 2, 3, 4], 0)])
class TestSolution:
    def test_differenceOfSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.differenceOfSum(
                nums,
            )
            == output
        )
