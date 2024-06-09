import pytest
from q_1537_getTheMaximumScore import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([2, 4, 5, 8, 10], [4, 6, 8, 9], 30),
        ([1, 3, 5, 7, 9], [3, 5, 100], 109),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 40),
    ],
)
class TestSolution:
    def test_maxSum(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSum(
                nums1,
                nums2,
            )
            == output
        )
