import pytest
from q_2678_numberOfSeniorCitizens import Solution


@pytest.mark.parametrize(
    "details, output",
    [
        (["7868190130M7522", "5303914400F9211", "9273338290F4010"], 2),
        (["1313579440F2036", "2921522980M5644"], 0),
    ],
)
class TestSolution:
    def test_countSeniors(self, details: List[str], output: int):
        sc = Solution()
        assert (
            sc.countSeniors(
                details,
            )
            == output
        )
