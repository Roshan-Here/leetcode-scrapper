import pytest
from q_0929_uniqueEmailAddresses import Solution


@pytest.mark.parametrize(
    "emails, output",
    [
        (
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ],
            2,
        ),
        (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
    ],
)
class TestSolution:
    def test_numUniqueEmails(self, emails: List[str], output: int):
        sc = Solution()
        assert (
            sc.numUniqueEmails(
                emails,
            )
            == output
        )
