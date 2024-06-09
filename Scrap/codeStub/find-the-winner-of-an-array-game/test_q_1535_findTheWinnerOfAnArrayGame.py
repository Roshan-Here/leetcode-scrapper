import pytest
from q_1535_findTheWinnerOfAnArrayGame import Solution


@pytest.mark.parametrize(
    "arr, k, output", [([2, 1, 3, 5, 4, 6, 7], 2, 5), ([3, 2, 1], 10, 3)]
)
class TestSolution:
    def test_getWinner(self, arr: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.getWinner(
                arr,
                k,
            )
            == output
        )
