import pytest
from q_2943_maximizeAreaOfSquareHoleInGrid import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int], output: int
    ):
        sc = Solution()
        assert sc.maximizeSquareHoleArea() == output
