import pytest
from q_1655_distributeRepeatingIntegers import Solution


@pytest.mark.parametrize(
    "nums, quantity, output",
    [
        ([1, 2, 3, 4], [2], False),
        ([1, 2, 3, 3], [2], True),
        ([1, 1, 2, 2], [2, 2], True),
    ],
)
class TestSolution:
    def test_canDistribute(self, nums: List[int], quantity: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canDistribute(
                nums,
                quantity,
            )
            == output
        )
