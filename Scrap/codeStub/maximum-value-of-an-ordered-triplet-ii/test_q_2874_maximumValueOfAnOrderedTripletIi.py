import pytest
from q_2874_maximumValueOfAnOrderedTripletIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([12, 6, 1, 2, 7], 77), ([1, 10, 3, 4, 19], 133), ([1, 2, 3], 0)]
)
class TestSolution:
    def test_maximumTripletValue(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumTripletValue(
                nums,
            )
            == output
        )
