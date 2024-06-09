import pytest
from q_2677_chunkArray import Solution


@pytest.mark.parametrize(
    "arr, size, output",
    [
        ([1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]),
        ([1, 9, 6, 3, 2], 3, [[1, 9, 6], [3, 2]]),
        ([8, 5, 3, 2, 6], 6, [[8, 5, 3, 2, 6]]),
        ([], 1, []),
    ],
)
class TestSolution:
    def test_chunkArray(self, output: Any):
        sc = Solution()
        assert (
            sc.chunkArray(
                arr,
                size,
            )
            == output
        )
