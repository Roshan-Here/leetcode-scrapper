import pytest
from q_0661_imageSmoother import Solution


@pytest.mark.parametrize(
    "img, output",
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        (
            [[100, 200, 100], [200, 50, 200], [100, 200, 100]],
            [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
        ),
    ],
)
class TestSolution:
    def test_imageSmoother(self, img: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.imageSmoother(
                img,
            )
            == output
        )
