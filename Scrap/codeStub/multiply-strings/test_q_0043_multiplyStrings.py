import pytest
from q_0043_multiplyStrings import Solution


@pytest.mark.parametrize(
    "num1, num2, output", [("2", "3", "6"), ("123", "456", "56088")]
)
class TestSolution:
    def test_multiply(self, num1: str, num2: str, output: str):
        sc = Solution()
        assert (
            sc.multiply(
                num1,
                num2,
            )
            == output
        )
