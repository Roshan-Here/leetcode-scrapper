import pytest
from q_0334_increasingTripletSubsequence import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4, 5], True), ([5, 4, 3, 2, 1], False), ([2, 1, 5, 0, 4, 6], True)],
)
class TestSolution:
    def test_increasingTriplet(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.increasingTriplet(
                nums,
            )
            == output
        )
