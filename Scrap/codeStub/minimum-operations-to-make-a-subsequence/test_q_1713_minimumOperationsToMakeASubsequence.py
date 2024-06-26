import pytest
from q_1713_minimumOperationsToMakeASubsequence import Solution


@pytest.mark.parametrize(
    "target, arr, output",
    [
        ([5, 1, 3], [9, 4, 2, 3, 4], 2),
        ([6, 4, 8, 1, 3, 2], [4, 7, 6, 2, 3, 8, 6, 1], 3),
    ],
)
class TestSolution:
    def test_minOperations(self, target: List[int], arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                target,
                arr,
            )
            == output
        )
