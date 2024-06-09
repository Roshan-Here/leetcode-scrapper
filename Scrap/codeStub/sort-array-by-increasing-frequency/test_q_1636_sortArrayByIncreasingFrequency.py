import pytest
from q_1636_sortArrayByIncreasingFrequency import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
        ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
        ([-1, 1, -6, 4, 5, -6, 1, 4, 1], [5, -1, 4, 4, -6, -6, 1, 1, 1]),
    ],
)
class TestSolution:
    def test_frequencySort(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.frequencySort(
                nums,
            )
            == output
        )
