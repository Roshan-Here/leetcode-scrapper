import pytest
from q_0202_happyNumber import Solution


@pytest.mark.parametrize("n, output", [(19, True), (2, False)])
class TestSolution:
    def test_isHappy(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isHappy(
                n,
            )
            == output
        )
