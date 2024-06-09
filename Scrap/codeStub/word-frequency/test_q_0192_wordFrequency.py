import pytest
from q_0192_wordFrequency import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_wordFrequency(self, output: Any):
        sc = Solution()
        assert sc.wordFrequency() == output
