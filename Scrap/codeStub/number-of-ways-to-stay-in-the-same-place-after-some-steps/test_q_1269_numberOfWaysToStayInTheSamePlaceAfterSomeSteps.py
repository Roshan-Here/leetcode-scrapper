import pytest
from q_1269_numberOfWaysToStayInTheSamePlaceAfterSomeSteps import Solution


@pytest.mark.parametrize("steps, arrLen, output", [(3, 2, 4), (2, 4, 2), (4, 2, 8)])
class TestSolution:
    def test_numWays(self, steps: int, arrLen: int, output: int):
        sc = Solution()
        assert (
            sc.numWays(
                steps,
                arrLen,
            )
            == output
        )
