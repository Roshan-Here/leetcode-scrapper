import pytest
from q_0991_brokenCalculator import Solution


@pytest.mark.parametrize(
    "startValue, target, output", [(2, 3, 2), (5, 8, 2), (3, 10, 3)]
)
class TestSolution:
    def test_brokenCalc(self, startValue: int, target: int, output: int):
        sc = Solution()
        assert (
            sc.brokenCalc(
                startValue,
                target,
            )
            == output
        )
