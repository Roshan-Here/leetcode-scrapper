import pytest
from q_2895_minimumProcessingTime import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minProcessingTime(
        self, processorTime: List[int], tasks: List[int], output: int
    ):
        sc = Solution()
        assert sc.minProcessingTime() == output
