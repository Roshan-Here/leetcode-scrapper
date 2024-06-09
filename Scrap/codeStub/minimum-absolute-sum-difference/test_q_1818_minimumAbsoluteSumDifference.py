import pytest
from q_1818_minimumAbsoluteSumDifference import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([1, 7, 5], [2, 3, 5], 3),
        ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10], 0),
        ([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4], 20),
    ],
)
class TestSolution:
    def test_minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minAbsoluteSumDiff(
                nums1,
                nums2,
            )
            == output
        )
