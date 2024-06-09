import pytest
from q_0012_integerToRoman import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_intToRoman(self, num: int, output: str):
        sc = Solution()
        assert sc.intToRoman() == output
