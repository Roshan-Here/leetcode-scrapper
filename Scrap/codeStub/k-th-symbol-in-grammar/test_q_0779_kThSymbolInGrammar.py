import pytest
from q_0779_kThSymbolInGrammar import Solution


@pytest.mark.parametrize("n, k, output", [(1, 1, 0), (2, 1, 0), (2, 2, 1)])
class TestSolution:
    def test_kthGrammar(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.kthGrammar(
                n,
                k,
            )
            == output
        )
