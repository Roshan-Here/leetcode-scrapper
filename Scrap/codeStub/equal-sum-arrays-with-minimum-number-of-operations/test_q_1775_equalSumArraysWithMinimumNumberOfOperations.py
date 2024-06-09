import pytest
from q_1775_equalSumArraysWithMinimumNumberOfOperations import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2], 3),
        ([1, 1, 1, 1, 1, 1, 1], [6], -1),
        ([6, 6], [1], 3),
    ],
)
class TestSolution:
    def test_minOperations(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums1,
                nums2,
            )
            == output
        )
