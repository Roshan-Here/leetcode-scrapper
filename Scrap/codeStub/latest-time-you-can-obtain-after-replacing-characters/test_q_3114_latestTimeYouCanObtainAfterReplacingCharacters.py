import pytest
from q_3114_latestTimeYouCanObtainAfterReplacingCharacters import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findLatestTime(self, s: str, output: str):
        sc = Solution()
        assert sc.findLatestTime() == output
