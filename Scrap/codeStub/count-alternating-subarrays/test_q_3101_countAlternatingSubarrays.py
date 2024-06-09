import pytest
from q_3101_countAlternatingSubarrays import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_countAlternatingSubarrays(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.countAlternatingSubarrays() == output
