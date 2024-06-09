import pytest
from q_2415_reverseOddLevelsOfBinaryTree import Solution


@pytest.mark.parametrize(
    "root, output",
    [
        ([2, 3, 5, 8, 13, 21, 34], [2, 5, 3, 8, 13, 21, 34]),
        ([7, 13, 11], [7, 11, 13]),
        (
            [0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
            [0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1],
        ),
    ],
)
class TestSolution:
    def test_reverseOddLevels(
        self, root: Optional[TreeNode], output: Optional[TreeNode]
    ):
        sc = Solution()
        assert (
            sc.reverseOddLevels(
                root,
            )
            == output
        )
