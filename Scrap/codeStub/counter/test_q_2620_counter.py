import pytest
from q_2620_counter import Solution


@pytest.mark.parametrize("output", [([10, 11, 12]), ([-2, -1, 0, 1, 2])])
class TestSolution:
    def test_counter(self, output: Any):
        sc = Solution()
        assert sc.counter() == output
