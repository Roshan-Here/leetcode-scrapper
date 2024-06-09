import pytest
from q_1323_maximum69Number import Solution


@pytest.mark.parametrize("num, output", [(9669, 9969), (9996, 9999), (9999, 9999)])
class TestSolution:
    def test_maximum69Number(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.maximum69Number(
                num,
            )
            == output
        )
