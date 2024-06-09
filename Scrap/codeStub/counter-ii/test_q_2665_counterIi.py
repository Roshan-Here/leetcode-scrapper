import pytest
from q_2665_counterIi import Solution


@pytest.mark.parametrize(
    "init, calls, output",
    [
        (5, ["increment", "reset", "decrement"], [6, 5, 4]),
        (0, ["increment", "increment", "decrement", "reset", "reset"], [1, 2, 1, 0, 0]),
    ],
)
class TestSolution:
    def test_counterIi(self, output: Any):
        sc = Solution()
        assert (
            sc.counterIi(
                init,
                calls,
            )
            == output
        )
