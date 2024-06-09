import pytest
from q_3085_minimumDeletionsToMakeStringKSpecial import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumDeletions(self, word: str, k: int, output: int):
        sc = Solution()
        assert sc.minimumDeletions() == output
