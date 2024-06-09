import pytest
from q_0675_cutOffTreesForGolfEvent import Solution


@pytest.mark.parametrize(
    "forest, output",
    [
        ([[1, 2, 3], [0, 0, 4], [7, 6, 5]], 6),
        ([[1, 2, 3], [0, 0, 0], [7, 6, 5]], -1),
        ([[2, 3, 4], [0, 0, 5], [8, 7, 6]], 6),
    ],
)
class TestSolution:
    def test_cutOffTree(self, forest: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.cutOffTree(
                forest,
            )
            == output
        )
