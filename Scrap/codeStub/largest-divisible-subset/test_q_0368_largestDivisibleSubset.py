import pytest
from q_0368_largestDivisibleSubset import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3], [1, 2]), ([1, 2, 4, 8], [1, 2, 4, 8])]
)
class TestSolution:
    def test_largestDivisibleSubset(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.largestDivisibleSubset(
                nums,
            )
            == output
        )
