import pytest
from q_0492_constructTheRectangle import Solution


@pytest.mark.parametrize(
    "area, output", [(4, [2, 2]), (37, [37, 1]), (122122, [427, 286])]
)
class TestSolution:
    def test_constructRectangle(self, area: int, output: List[int]):
        sc = Solution()
        assert (
            sc.constructRectangle(
                area,
            )
            == output
        )
