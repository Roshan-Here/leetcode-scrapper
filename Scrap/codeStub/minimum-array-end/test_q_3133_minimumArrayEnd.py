import pytest
from q_3133_minimumArrayEnd import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minEnd(self, n: int, x: int, output: int):
        sc = Solution()
        assert sc.minEnd() == output
