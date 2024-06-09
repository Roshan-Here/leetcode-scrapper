import pytest
from q_0165_compareVersionNumbers import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_compareVersion(self, version1: str, version2: str, output: int):
        sc = Solution()
        assert sc.compareVersion() == output
