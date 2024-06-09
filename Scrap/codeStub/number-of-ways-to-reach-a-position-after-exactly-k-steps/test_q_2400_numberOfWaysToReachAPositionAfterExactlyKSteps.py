import pytest
from q_2400_numberOfWaysToReachAPositionAfterExactlyKSteps import Solution


@pytest.mark.parametrize("startPos, endPos, k, output", [(1, 2, 3, 3), (2, 5, 10, 0)])
class TestSolution:
    def test_numberOfWays(self, startPos: int, endPos: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfWays(
                startPos,
                endPos,
                k,
            )
            == output
        )
