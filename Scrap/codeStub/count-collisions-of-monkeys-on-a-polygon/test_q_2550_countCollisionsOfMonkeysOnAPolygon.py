import pytest
from q_2550_countCollisionsOfMonkeysOnAPolygon import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_monkeyMove(self, n: int, output: int):
        sc = Solution()
        assert sc.monkeyMove() == output
