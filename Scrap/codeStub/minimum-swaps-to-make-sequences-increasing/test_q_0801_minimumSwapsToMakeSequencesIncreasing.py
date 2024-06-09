import pytest
from q_0801_minimumSwapsToMakeSequencesIncreasing import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([1, 3, 5, 4], [1, 2, 3, 7], 1), ([0, 3, 5, 8, 9], [2, 1, 4, 6, 9], 1)],
)
class TestSolution:
    def test_minSwap(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSwap(
                nums1,
                nums2,
            )
            == output
        )
