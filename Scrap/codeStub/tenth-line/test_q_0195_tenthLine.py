import pytest
from q_0195_tenthLine import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_tenthLine(self, output: Any):
        sc = Solution()
        assert sc.tenthLine() == output
