import pytest
from q_0365_waterAndJugProblem import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_canMeasureWater(self, x: int, y: int, target: int, output: bool):
        sc = Solution()
        assert sc.canMeasureWater() == output
