import pytest
from q_0071_simplifyPath import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_simplifyPath(self, path: str, output: str):
        sc = Solution()
        assert sc.simplifyPath() == output
