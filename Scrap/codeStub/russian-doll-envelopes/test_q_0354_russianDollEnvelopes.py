import pytest
from q_0354_russianDollEnvelopes import Solution


@pytest.mark.parametrize(
    "envelopes, output",
    [([[5, 4], [6, 4], [6, 7], [2, 3]], 3), ([[1, 1], [1, 1], [1, 1]], 1)],
)
class TestSolution:
    def test_maxEnvelopes(self, envelopes: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxEnvelopes(
                envelopes,
            )
            == output
        )
