import pytest
from q_0939_minimumAreaRectangle import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]], 4),
        ([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]], 2),
    ],
)
class TestSolution:
    def test_minAreaRect(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minAreaRect(
                points,
            )
            == output
        )
