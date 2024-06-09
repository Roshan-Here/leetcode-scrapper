import pytest
from q_1764_formArrayByConcatenatingSubarraysOfAnotherArray import Solution


@pytest.mark.parametrize(
    "groups, nums, output",
    [
        ([[1, -1, -1], [3, -2, 0]], [1, -1, 0, 1, -1, -1, 3, -2, 0], True),
        ([[10, -2], [1, 2, 3, 4]], [1, 2, 3, 4, 10, -2], False),
        ([[1, 2, 3], [3, 4]], [7, 7, 1, 2, 3, 4, 7, 7], False),
    ],
)
class TestSolution:
    def test_canChoose(self, groups: List[List[int]], nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canChoose(
                groups,
                nums,
            )
            == output
        )
