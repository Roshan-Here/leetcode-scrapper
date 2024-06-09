import pytest
from q_1043_partitionArrayForMaximumSum import Solution


@pytest.mark.parametrize(
    "arr, k, output",
    [
        ([1, 15, 7, 9, 2, 5, 10], 3, 84),
        ([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4, 83),
        ([1], 1, 1),
    ],
)
class TestSolution:
    def test_maxSumAfterPartitioning(self, arr: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxSumAfterPartitioning(
                arr,
                k,
            )
            == output
        )
