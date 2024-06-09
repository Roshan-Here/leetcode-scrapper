import pytest
from q_0621_taskScheduler import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_leastInterval(self, tasks: List[str], n: int, output: int):
        sc = Solution()
        assert sc.leastInterval() == output
