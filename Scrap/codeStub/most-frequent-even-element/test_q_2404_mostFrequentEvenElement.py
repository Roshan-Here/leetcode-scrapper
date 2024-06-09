import pytest
from q_2404_mostFrequentEvenElement import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([0, 1, 2, 2, 4, 4, 1], 2),
        ([4, 4, 4, 9, 2, 4], 4),
        ([29, 47, 21, 41, 13, 37, 25, 7], -1),
    ],
)
class TestSolution:
    def test_mostFrequentEven(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.mostFrequentEven(
                nums,
            )
            == output
        )
