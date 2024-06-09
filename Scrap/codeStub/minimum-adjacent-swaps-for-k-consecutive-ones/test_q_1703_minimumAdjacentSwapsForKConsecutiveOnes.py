import pytest
from q_1703_minimumAdjacentSwapsForKConsecutiveOnes import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 0, 0, 1, 0, 1], 2, 1),
        ([1, 0, 0, 0, 0, 0, 1, 1], 3, 5),
        ([1, 1, 0, 1], 2, 0),
    ],
)
class TestSolution:
    def test_minMoves(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minMoves(
                nums,
                k,
            )
            == output
        )
