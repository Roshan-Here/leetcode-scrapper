import pytest
from q_2899_lastVisitedIntegers import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_lastVisitedIntegers(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert sc.lastVisitedIntegers() == output
