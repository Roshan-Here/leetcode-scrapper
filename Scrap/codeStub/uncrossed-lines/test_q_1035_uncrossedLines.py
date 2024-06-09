import pytest
from q_1035_uncrossedLines import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ],
)
class TestSolution:
    def test_maxUncrossedLines(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxUncrossedLines(
                nums1,
                nums2,
            )
            == output
        )
