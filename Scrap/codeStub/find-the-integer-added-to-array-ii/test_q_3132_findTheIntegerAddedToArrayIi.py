import pytest
from q_3132_findTheIntegerAddedToArrayIi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumAddedInteger(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert sc.minimumAddedInteger() == output
