import pytest
from q_0765_couplesHoldingHands import Solution


@pytest.mark.parametrize("row, output", [([0, 2, 1, 3], 1), ([3, 2, 0, 1], 0)])
class TestSolution:
    def test_minSwapsCouples(self, row: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSwapsCouples(
                row,
            )
            == output
        )
