import pytest
from q_3131_findTheIntegerAddedToArrayI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_addedInteger(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert sc.addedInteger() == output
