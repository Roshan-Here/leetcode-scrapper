import pytest
from q_3019_numberOfChangingKeys import Solution


@pytest.mark.parametrize("s, output", [("aAbBcC", 2), ("AaAaAaaA", 0)])
class TestSolution:
    def test_countKeyChanges(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countKeyChanges(
                s,
            )
            == output
        )
