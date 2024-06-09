import pytest
from q_3137_minimumNumberOfOperationsToMakeWordKPeriodic import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumOperationsToMakeKPeriodic(self, word: str, k: int, output: int):
        sc = Solution()
        assert sc.minimumOperationsToMakeKPeriodic() == output
