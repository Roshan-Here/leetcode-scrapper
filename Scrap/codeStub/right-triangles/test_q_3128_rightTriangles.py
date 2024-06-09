import pytest
from q_3128_rightTriangles import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfRightTriangles(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert sc.numberOfRightTriangles() == output
