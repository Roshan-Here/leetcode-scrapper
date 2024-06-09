import pytest
from q_2191_sortTheJumbledNumbers import Solution


@pytest.mark.parametrize(
    "mapping, nums, output",
    [
        ([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38], [338, 38, 991]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123], [123, 456, 789]),
    ],
)
class TestSolution:
    def test_sortJumbled(self, mapping: List[int], nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortJumbled(
                mapping,
                nums,
            )
            == output
        )
