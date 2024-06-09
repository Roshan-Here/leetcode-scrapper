import pytest
from q_1679_maxNumberOfKSumPairs import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 3, 4], 5, 2), ([3, 1, 3, 4, 3], 6, 1)]
)
class TestSolution:
    def test_maxOperations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxOperations(
                nums,
                k,
            )
            == output
        )
