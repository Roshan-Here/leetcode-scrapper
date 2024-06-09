import pytest
from q_0818_raceCar import Solution


@pytest.mark.parametrize("target, output", [(3, 2), (6, 5)])
class TestSolution:
    def test_racecar(self, target: int, output: int):
        sc = Solution()
        assert (
            sc.racecar(
                target,
            )
            == output
        )
