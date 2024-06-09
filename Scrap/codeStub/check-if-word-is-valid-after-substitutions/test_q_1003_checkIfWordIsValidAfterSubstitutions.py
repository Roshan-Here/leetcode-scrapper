import pytest
from q_1003_checkIfWordIsValidAfterSubstitutions import Solution


@pytest.mark.parametrize(
    "s, output", [("aabcbc", True), ("abcabcababcc", True), ("abccba", False)]
)
class TestSolution:
    def test_isValid(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.isValid(
                s,
            )
            == output
        )
