import pytest
from q_1691_maximumHeightByStackingCuboids import Solution


@pytest.mark.parametrize(
    "cuboids, output",
    [
        ([[50, 45, 20], [95, 37, 53], [45, 23, 12]], 190),
        ([[38, 25, 45], [76, 35, 3]], 76),
        (
            [
                [7, 11, 17],
                [7, 17, 11],
                [11, 7, 17],
                [11, 17, 7],
                [17, 7, 11],
                [17, 11, 7],
            ],
            102,
        ),
    ],
)
class TestSolution:
    def test_maxHeight(self, cuboids: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxHeight(
                cuboids,
            )
            == output
        )
