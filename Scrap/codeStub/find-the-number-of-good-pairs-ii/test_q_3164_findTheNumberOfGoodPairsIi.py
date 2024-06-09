import pytest
from q_3164_findTheNumberOfGoodPairsIi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfPairs(
        self, nums1: List[int], nums2: List[int], k: int, output: int
    ):
        sc = Solution()
        assert sc.numberOfPairs() == output
