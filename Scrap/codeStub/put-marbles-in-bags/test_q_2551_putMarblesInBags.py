import pytest
from q_2551_putMarblesInBags import Solution


@pytest.mark.parametrize("weights, k, output", [([1, 3, 5, 1], 2, 4), ([1, 3], 2, 0)])
class TestSolution:
    def test_putMarbles(self, weights: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.putMarbles(
                weights,
                k,
            )
            == output
        )
