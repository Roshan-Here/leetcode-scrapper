import pytest
from q_1140_stoneGameIi import Solution


@pytest.mark.parametrize(
    "piles, output", [([2, 7, 9, 4, 4], 10), ([1, 2, 3, 4, 5, 100], 104)]
)
class TestSolution:
    def test_stoneGameII(self, piles: List[int], output: int):
        sc = Solution()
        assert (
            sc.stoneGameII(
                piles,
            )
            == output
        )
