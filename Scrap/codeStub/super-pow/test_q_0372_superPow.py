import pytest
from q_0372_superPow import Solution


@pytest.mark.parametrize(
    "a, b, output", [(2, [3], 8), (2, [1, 0], 1024), (1, [4, 3, 3, 8, 5, 2], 1)]
)
class TestSolution:
    def test_superPow(self, a: int, b: List[int], output: int):
        sc = Solution()
        assert (
            sc.superPow(
                a,
                b,
            )
            == output
        )
