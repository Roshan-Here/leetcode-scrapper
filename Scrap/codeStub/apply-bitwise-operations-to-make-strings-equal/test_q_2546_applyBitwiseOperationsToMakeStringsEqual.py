import pytest
from q_2546_applyBitwiseOperationsToMakeStringsEqual import Solution


@pytest.mark.parametrize(
    "s, target, output", [("1010", "0110", True), ("11", "00", False)]
)
class TestSolution:
    def test_makeStringsEqual(self, s: str, target: str, output: bool):
        sc = Solution()
        assert (
            sc.makeStringsEqual(
                s,
                target,
            )
            == output
        )
