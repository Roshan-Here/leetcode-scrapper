import pytest
from q_2022_convert1DArrayInto2DArray import Solution


@pytest.mark.parametrize(
    "original, m, n, output",
    [
        ([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]]),
        ([1, 2, 3], 1, 3, [[1, 2, 3]]),
        ([1, 2], 1, 1, []),
    ],
)
class TestSolution:
    def test_construct2DArray(
        self, original: List[int], m: int, n: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.construct2DArray(
                original,
                m,
                n,
            )
            == output
        )
