import pytest
from q_0069_sqrtx import Solution


@pytest.mark.parametrize("x, output", [(4, 2), (8, 2)])
class TestSolution:
    def test_mySqrt(self, x: int, output: int):
        sc = Solution()
        assert (
            sc.mySqrt(
                x,
            )
            == output
        )
