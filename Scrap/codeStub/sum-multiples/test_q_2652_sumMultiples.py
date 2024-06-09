import pytest
from q_2652_sumMultiples import Solution


@pytest.mark.parametrize("n, output", [(7, 21), (10, 40), (9, 30)])
class TestSolution:
    def test_sumOfMultiples(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.sumOfMultiples(
                n,
            )
            == output
        )
