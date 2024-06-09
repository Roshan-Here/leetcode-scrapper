import pytest
from q_2836_maximizeValueOfFunctionInABallPassingGame import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_getMaxFunctionValue(self, receiver: List[int], k: int, output: int):
        sc = Solution()
        assert sc.getMaxFunctionValue() == output
