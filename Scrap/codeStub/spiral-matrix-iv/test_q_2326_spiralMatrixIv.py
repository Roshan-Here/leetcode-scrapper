import pytest
from q_2326_spiralMatrixIv import Solution


@pytest.mark.parametrize(
    "m, n, head, output",
    [
        (
            3,
            5,
            [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0],
            [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]],
        ),
        (1, 4, [0, 1, 2], [[0, 1, 2, -1]]),
    ],
)
class TestSolution:
    def test_spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.spiralMatrix(
                m,
                n,
                head,
            )
            == output
        )
