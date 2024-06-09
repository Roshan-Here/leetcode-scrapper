import pytest
from q_2179_countGoodTripletsInAnArray import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([2, 0, 1, 3], [0, 1, 2, 3], 1), ([4, 0, 1, 3, 2], [4, 1, 0, 2, 3], 4)],
)
class TestSolution:
    def test_goodTriplets(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.goodTriplets(
                nums1,
                nums2,
            )
            == output
        )
