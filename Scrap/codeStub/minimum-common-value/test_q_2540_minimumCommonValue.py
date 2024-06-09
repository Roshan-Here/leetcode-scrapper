import pytest
from q_2540_minimumCommonValue import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output", [([1, 2, 3], [2, 4], 2), ([1, 2, 3, 6], [2, 3, 4, 5], 2)]
)
class TestSolution:
    def test_getCommon(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.getCommon(
                nums1,
                nums2,
            )
            == output
        )
