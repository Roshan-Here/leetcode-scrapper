import pytest
from q_0955_deleteColumnsToMakeSortedIi import Solution


@pytest.mark.parametrize(
    "strs, output",
    [(["ca", "bb", "ac"], 1), (["xc", "yb", "za"], 0), (["zyx", "wvu", "tsr"], 3)],
)
class TestSolution:
    def test_minDeletionSize(self, strs: List[str], output: int):
        sc = Solution()
        assert (
            sc.minDeletionSize(
                strs,
            )
            == output
        )
