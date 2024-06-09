import pytest
from q_0917_reverseOnlyLetters import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
    ],
)
class TestSolution:
    def test_reverseOnlyLetters(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.reverseOnlyLetters(
                s,
            )
            == output
        )
