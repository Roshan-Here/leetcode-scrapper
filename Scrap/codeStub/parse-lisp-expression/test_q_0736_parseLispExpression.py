import pytest
from q_0736_parseLispExpression import Solution


@pytest.mark.parametrize(
    "expression, output",
    [
        ("(let x 2 (mult x (let x 3 y 4 (add x y))))", 14),
        ("(let x 3 x 2 x)", 2),
        ("(let x 1 y 2 x (add x y) (add x y))", 5),
    ],
)
class TestSolution:
    def test_evaluate(self, expression: str, output: int):
        sc = Solution()
        assert (
            sc.evaluate(
                expression,
            )
            == output
        )
