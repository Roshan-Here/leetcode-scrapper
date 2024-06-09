import pytest
from q_0768_maxChunksToMakeSortedIi import Solution


@pytest.mark.parametrize("arr, output", [([5, 4, 3, 2, 1], 1), ([2, 1, 3, 4, 4], 4)])
class TestSolution:
    def test_maxChunksToSorted(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxChunksToSorted(
                arr,
            )
            == output
        )
