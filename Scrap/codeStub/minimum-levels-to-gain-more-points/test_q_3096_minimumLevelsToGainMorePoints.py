import pytest
from q_3096_minimumLevelsToGainMorePoints import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumLevels(self, possible: List[int], output: int):
        sc = Solution()
        assert sc.minimumLevels() == output
