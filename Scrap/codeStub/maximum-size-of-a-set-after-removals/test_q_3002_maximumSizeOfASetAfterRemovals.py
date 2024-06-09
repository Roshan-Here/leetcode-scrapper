import pytest
from q_3002_maximumSizeOfASetAfterRemovals import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([1, 2, 1, 2], [1, 1, 1, 1], 2),
        ([1, 2, 3, 4, 5, 6], [2, 3, 2, 3, 2, 3], 5),
        ([1, 1, 2, 2, 3, 3], [4, 4, 5, 5, 6, 6], 6),
    ],
)
class TestSolution:
    def test_maximumSetSize(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumSetSize(
                nums1,
                nums2,
            )
            == output
        )
