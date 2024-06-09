import pytest
from q_2283_checkIfNumberHasEqualDigitCountAndDigitValue import Solution


@pytest.mark.parametrize("num, output", [("1210", True), ("030", False)])
class TestSolution:
    def test_digitCount(self, num: str, output: bool):
        sc = Solution()
        assert (
            sc.digitCount(
                num,
            )
            == output
        )
