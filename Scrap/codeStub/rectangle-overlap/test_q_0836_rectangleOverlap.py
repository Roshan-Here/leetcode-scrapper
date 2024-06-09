import pytest
from q_0836_rectangleOverlap import Solution


@pytest.mark.parametrize(
    "rec1, rec2, output",
    [
        ([0, 0, 2, 2], [1, 1, 3, 3], True),
        ([0, 0, 1, 1], [1, 0, 2, 1], False),
        ([0, 0, 1, 1], [2, 2, 3, 3], False),
    ],
)
class TestSolution:
    def test_isRectangleOverlap(self, rec1: List[int], rec2: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isRectangleOverlap(
                rec1,
                rec2,
            )
            == output
        )
