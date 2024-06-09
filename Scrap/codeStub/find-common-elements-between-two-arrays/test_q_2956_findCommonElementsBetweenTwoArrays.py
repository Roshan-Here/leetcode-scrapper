import pytest
from q_2956_findCommonElementsBetweenTwoArrays import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findIntersectionValues(
        self, nums1: List[int], nums2: List[int], output: List[int]
    ):
        sc = Solution()
        assert sc.findIntersectionValues() == output
