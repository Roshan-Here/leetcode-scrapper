import pytest
from q_2911_minimumChangesToMakeKSemiPalindromes import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumChanges(self, s: str, k: int, output: int):
        sc = Solution()
        assert sc.minimumChanges() == output
