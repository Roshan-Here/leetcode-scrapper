import pytest
from q_3145_findProductsOfElementsOfBigArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findProductsOfElements(self, queries: List[List[int]], output: List[int]):
        sc = Solution()
        assert sc.findProductsOfElements() == output
