import pytest
from q_1980_findUniqueBinaryString import Solution


@pytest.mark.parametrize(
    "nums, output",
    [(["01", "10"], "11"), (["00", "01"], "11"), (["111", "011", "001"], "101")],
)
class TestSolution:
    def test_findDifferentBinaryString(self, nums: List[str], output: str):
        sc = Solution()
        assert (
            sc.findDifferentBinaryString(
                nums,
            )
            == output
        )
