import pytest
from q_0791_customSortString import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_customSortString(self, order: str, s: str, output: str):
        sc = Solution()
        assert sc.customSortString() == output
