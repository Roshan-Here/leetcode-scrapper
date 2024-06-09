import pytest
from q_0464_canIWin import Solution


@pytest.mark.parametrize(
    "maxChoosableInteger, desiredTotal, output",
    [(10, 11, False), (10, 0, True), (10, 1, True)],
)
class TestSolution:
    def test_canIWin(self, maxChoosableInteger: int, desiredTotal: int, output: bool):
        sc = Solution()
        assert (
            sc.canIWin(
                maxChoosableInteger,
                desiredTotal,
            )
            == output
        )
