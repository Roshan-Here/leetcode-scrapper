import pytest
from q_3047_findTheLargestAreaOfSquareInsideTwoRectangles import Solution


@pytest.mark.parametrize(
    "bottomLeft, topRight, output",
    [
        ([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]], 1),
        ([[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]], 1),
        ([[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]], 0),
    ],
)
class TestSolution:
    def test_largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.largestSquareArea(
                bottomLeft,
                topRight,
            )
            == output
        )
