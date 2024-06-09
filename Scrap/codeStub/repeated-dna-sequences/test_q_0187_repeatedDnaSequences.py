import pytest
from q_0187_repeatedDnaSequences import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
        ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ],
)
class TestSolution:
    def test_findRepeatedDnaSequences(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.findRepeatedDnaSequences(
                s,
            )
            == output
        )
