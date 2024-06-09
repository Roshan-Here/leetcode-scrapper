import pytest
from q_2139_minimumMovesToReachTargetScore import Solution


@pytest.mark.parametrize(
    "target, maxDoubles, output", [(5, 0, 4), (19, 2, 7), (10, 4, 4)]
)
class TestSolution:
    def test_minMoves(self, target: int, maxDoubles: int, output: int):
        sc = Solution()
        assert (
            sc.minMoves(
                target,
                maxDoubles,
            )
            == output
        )
