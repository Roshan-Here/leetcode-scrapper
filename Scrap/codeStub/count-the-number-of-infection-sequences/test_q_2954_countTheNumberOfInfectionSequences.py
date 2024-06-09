import pytest
from q_2954_countTheNumberOfInfectionSequences import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfSequence(self, n: int, sick: List[int], output: int):
        sc = Solution()
        assert sc.numberOfSequence() == output
