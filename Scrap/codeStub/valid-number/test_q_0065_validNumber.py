import pytest
from q_0065_validNumber import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_isNumber(self, s: str, output: bool):
        sc = Solution()
        assert sc.isNumber() == output
