import pytest
from q_2053_kthDistinctStringInAnArray import Solution


@pytest.mark.parametrize(
    "arr, k, output",
    [
        (["d", "b", "c", "b", "c", "a"], 2, "a"),
        (["aaa", "aa", "a"], 1, "aaa"),
        (["a", "b", "a"], 3, ""),
    ],
)
class TestSolution:
    def test_kthDistinct(self, arr: List[str], k: int, output: str):
        sc = Solution()
        assert (
            sc.kthDistinct(
                arr,
                k,
            )
            == output
        )
