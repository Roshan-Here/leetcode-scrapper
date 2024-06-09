import pytest
from q_1642_furthestBuildingYouCanReach import Solution


@pytest.mark.parametrize(
    "heights, bricks, ladders, output",
    [
        ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([14, 3, 19, 3], 17, 0, 3),
    ],
)
class TestSolution:
    def test_furthestBuilding(
        self, heights: List[int], bricks: int, ladders: int, output: int
    ):
        sc = Solution()
        assert (
            sc.furthestBuilding(
                heights,
                bricks,
                ladders,
            )
            == output
        )
