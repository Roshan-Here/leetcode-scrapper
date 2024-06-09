import pytest
from q_1089_duplicateZeros import Solution


@pytest.mark.parametrize(
    "arr, output",
    [([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]), ([1, 2, 3], [1, 2, 3])],
)
class TestSolution:
    def test_duplicateZeros(self, arr: List[int], output: None):
        sc = Solution()
        assert (
            sc.duplicateZeros(
                arr,
            )
            == output
        )
