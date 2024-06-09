import pytest
from q_2585_numberOfWaysToEarnPoints import Solution


@pytest.mark.parametrize(
    "target, types, output",
    [
        (6, [[6, 1], [3, 2], [2, 3]], 7),
        (5, [[50, 1], [50, 2], [50, 5]], 4),
        (18, [[6, 1], [3, 2], [2, 3]], 1),
    ],
)
class TestSolution:
    def test_waysToReachTarget(self, target: int, types: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.waysToReachTarget(
                target,
                types,
            )
            == output
        )
