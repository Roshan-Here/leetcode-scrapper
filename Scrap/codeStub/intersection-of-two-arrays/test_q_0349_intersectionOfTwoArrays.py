import pytest
from q_0349_intersectionOfTwoArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([1, 2, 2, 1], [2, 2], [2]), ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4])],
)
class TestSolution:
    def test_intersection(self, nums1: List[int], nums2: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.intersection(
                nums1,
                nums2,
            )
            == output
        )
