import pytest
from q_2917_findTheKOrOfAnArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findKOr(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert sc.findKOr() == output
