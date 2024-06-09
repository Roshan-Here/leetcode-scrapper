import pytest
from q_1816_truncateSentence import Solution


@pytest.mark.parametrize(
    "s, k, output",
    [
        ("Hello how are you Contestant", 4, "Hello how are you"),
        ("What is the solution to this problem", 4, "What is the solution"),
        ("chopper is not a tanuki", 5, "chopper is not a tanuki"),
    ],
)
class TestSolution:
    def test_truncateSentence(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.truncateSentence(
                s,
                k,
            )
            == output
        )
