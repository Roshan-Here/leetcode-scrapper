import pytest
from q_0282_expressionAddOperators import Solution


@pytest.mark.parametrize(
    "num, target, output",
    [
        ("123", 6, ["1*2*3", "1+2+3"]),
        ("232", 8, ["2*3+2", "2+3*2"]),
        ("3456237490", 9191, []),
    ],
)
class TestSolution:
    def test_addOperators(self, num: str, target: int, output: List[str]):
        sc = Solution()
        assert (
            sc.addOperators(
                num,
                target,
            )
            == output
        )
