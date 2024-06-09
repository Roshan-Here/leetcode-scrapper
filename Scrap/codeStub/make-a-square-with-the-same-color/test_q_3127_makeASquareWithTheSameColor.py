import pytest
from q_3127_makeASquareWithTheSameColor import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_canMakeSquare(self, grid: List[List[str]], output: bool):
        sc = Solution()
        assert sc.canMakeSquare() == output
