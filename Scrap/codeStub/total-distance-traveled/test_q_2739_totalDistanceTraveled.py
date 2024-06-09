import pytest
from q_2739_totalDistanceTraveled import Solution


@pytest.mark.parametrize("mainTank, additionalTank, output", [(5, 10, 60), (1, 2, 10)])
class TestSolution:
    def test_distanceTraveled(self, mainTank: int, additionalTank: int, output: int):
        sc = Solution()
        assert (
            sc.distanceTraveled(
                mainTank,
                additionalTank,
            )
            == output
        )
