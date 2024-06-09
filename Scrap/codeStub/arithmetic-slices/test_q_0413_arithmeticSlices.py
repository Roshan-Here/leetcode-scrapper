import pytest
from q_0413_arithmeticSlices import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3, 4], 3), ([1], 0)])
class TestSolution:
    def test_numberOfArithmeticSlices(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfArithmeticSlices(
                nums,
            )
            == output
        )
