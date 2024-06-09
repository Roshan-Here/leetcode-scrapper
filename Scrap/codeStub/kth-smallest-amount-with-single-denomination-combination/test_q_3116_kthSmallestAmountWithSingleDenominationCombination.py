import pytest
from q_3116_kthSmallestAmountWithSingleDenominationCombination import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findKthSmallest(self, coins: List[int], k: int, output: int):
        sc = Solution()
        assert sc.findKthSmallest() == output
