import pytest
from q_0008_stringToIntegerAtoi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_myAtoi(self, s: str, output: int):
        sc = Solution()
        assert sc.myAtoi() == output
