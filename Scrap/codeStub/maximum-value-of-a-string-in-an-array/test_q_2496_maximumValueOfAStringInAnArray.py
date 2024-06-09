import pytest
from q_2496_maximumValueOfAStringInAnArray import Solution


@pytest.mark.parametrize(
    "strs, output",
    [(["alic3", "bob", "3", "4", "00000"], 5), (["1", "01", "001", "0001"], 1)],
)
class TestSolution:
    def test_maximumValue(self, strs: List[str], output: int):
        sc = Solution()
        assert (
            sc.maximumValue(
                strs,
            )
            == output
        )
