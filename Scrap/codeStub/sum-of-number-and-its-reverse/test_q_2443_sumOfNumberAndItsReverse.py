import pytest
from q_2443_sumOfNumberAndItsReverse import Solution


@pytest.mark.parametrize("num, output", [(443, True), (63, False), (181, True)])
class TestSolution:
    def test_sumOfNumberAndReverse(self, num: int, output: bool):
        sc = Solution()
        assert (
            sc.sumOfNumberAndReverse(
                num,
            )
            == output
        )
