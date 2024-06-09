import pytest
from q_0561_arrayPartition import Solution


@pytest.mark.parametrize("nums, output", [([1, 4, 3, 2], 4), ([6, 2, 6, 5, 1, 2], 9)])
class TestSolution:
    def test_arrayPairSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.arrayPairSum(
                nums,
            )
            == output
        )
