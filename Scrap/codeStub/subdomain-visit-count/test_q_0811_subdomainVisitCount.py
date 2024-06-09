import pytest
from q_0811_subdomainVisitCount import Solution


@pytest.mark.parametrize(
    "cpdomains, output",
    [
        (
            ["9001 discuss.leetcode.com"],
            ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"],
        ),
        (
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
            [
                "901 mail.com",
                "50 yahoo.com",
                "900 google.mail.com",
                "5 wiki.org",
                "5 org",
                "1 intel.mail.com",
                "951 com",
            ],
        ),
    ],
)
class TestSolution:
    def test_subdomainVisits(self, cpdomains: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.subdomainVisits(
                cpdomains,
            )
            == output
        )
