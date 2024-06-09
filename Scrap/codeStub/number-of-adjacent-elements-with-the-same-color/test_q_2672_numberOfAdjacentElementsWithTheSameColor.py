import pytest
from q_2672_numberOfAdjacentElementsWithTheSameColor import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_colorTheArray(self, n: int, queries: List[List[int]], output: List[int]):
        sc = Solution()
        assert sc.colorTheArray() == output
