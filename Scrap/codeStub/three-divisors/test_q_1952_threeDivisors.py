import pytest
from q_1952_threeDivisors import Solution


@pytest.mark.parametrize("n, output", [(2, False), (4, True)])
class TestSolution:
    def test_isThree(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isThree(
                n,
            )
            == output
        )
