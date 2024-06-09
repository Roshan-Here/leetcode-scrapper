import pytest
from q_2427_numberOfCommonFactors import Solution


@pytest.mark.parametrize("a, b, output", [(12, 6, 4), (25, 30, 2)])
class TestSolution:
    def test_commonFactors(self, a: int, b: int, output: int):
        sc = Solution()
        assert (
            sc.commonFactors(
                a,
                b,
            )
            == output
        )
