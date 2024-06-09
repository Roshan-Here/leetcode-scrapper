import pytest
from q_2206_divideArrayIntoEqualPairs import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 2, 3, 2, 2, 2], True), ([1, 2, 3, 4], False)]
)
class TestSolution:
    def test_divideArray(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.divideArray(
                nums,
            )
            == output
        )
