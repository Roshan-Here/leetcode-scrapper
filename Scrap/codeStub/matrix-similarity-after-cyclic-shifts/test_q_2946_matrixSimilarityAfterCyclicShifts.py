import pytest
from q_2946_matrixSimilarityAfterCyclicShifts import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_areSimilar(self, mat: List[List[int]], k: int, output: bool):
        sc = Solution()
        assert sc.areSimilar() == output
