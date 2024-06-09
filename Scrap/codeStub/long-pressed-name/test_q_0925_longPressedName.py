import pytest
from q_0925_longPressedName import Solution


@pytest.mark.parametrize(
    "name, typed, output", [("alex", "aaleex", True), ("saeed", "ssaaedd", False)]
)
class TestSolution:
    def test_isLongPressedName(self, name: str, typed: str, output: bool):
        sc = Solution()
        assert (
            sc.isLongPressedName(
                name,
                typed,
            )
            == output
        )
