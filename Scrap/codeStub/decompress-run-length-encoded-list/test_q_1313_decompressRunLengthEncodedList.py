import pytest
from q_1313_decompressRunLengthEncodedList import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4], [2, 4, 4, 4]), ([1, 1, 2, 3], [1, 3, 3])]
)
class TestSolution:
    def test_decompressRLElist(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.decompressRLElist(
                nums,
            )
            == output
        )
