import pytest
from q_3092_mostFrequentIds import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_mostFrequentIDs(self, nums: List[int], freq: List[int], output: List[int]):
        sc = Solution()
        assert sc.mostFrequentIDs() == output
