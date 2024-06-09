import pytest
from q_2810_faultyKeyboard import Solution


@pytest.mark.parametrize("s, output", [("string", "rtsng"), ("poiinter", "ponter")])
class TestSolution:
    def test_finalString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.finalString(
                s,
            )
            == output
        )
