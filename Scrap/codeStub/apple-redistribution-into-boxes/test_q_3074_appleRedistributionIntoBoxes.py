import pytest
from q_3074_appleRedistributionIntoBoxes import Solution


@pytest.mark.parametrize(
    "apple, capacity, output",
    [([1, 3, 2], [4, 3, 1, 5, 2], 2), ([5, 5, 5], [2, 4, 2, 7], 4)],
)
class TestSolution:
    def test_minimumBoxes(self, apple: List[int], capacity: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumBoxes(
                apple,
                capacity,
            )
            == output
        )
