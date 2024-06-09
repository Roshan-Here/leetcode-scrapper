import pytest
from q_2060_checkIfAnOriginalStringExistsGivenTwoEncodedStrings import Solution


@pytest.mark.parametrize(
    "s1, s2, output",
    [
        ("internationalization", "i18n", True),
        ("l123e", "44", True),
        ("a5b", "c5b", False),
    ],
)
class TestSolution:
    def test_possiblyEquals(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.possiblyEquals(
                s1,
                s2,
            )
            == output
        )
