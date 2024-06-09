import pytest
from q_0038_countAndSay import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_countAndSay(self, n: int, output: str):
        sc = Solution()
        assert sc.countAndSay() == output
