import pytest
from q_0877_stoneGame import Solution


@pytest.mark.parametrize("piles, output", [([5, 3, 4, 5], True), ([3, 7, 2, 3], True)])
class TestSolution:
    def test_stoneGame(self, piles: List[int], output: bool):
        sc = Solution()
        assert (
            sc.stoneGame(
                piles,
            )
            == output
        )
