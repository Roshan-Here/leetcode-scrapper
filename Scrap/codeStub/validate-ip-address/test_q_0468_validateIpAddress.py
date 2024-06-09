import pytest
from q_0468_validateIpAddress import Solution


@pytest.mark.parametrize(
    "queryIP, output",
    [
        ("172.16.254.1", "IPv4"),
        ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("256.256.256.256", "Neither"),
    ],
)
class TestSolution:
    def test_validIPAddress(self, queryIP: str, output: str):
        sc = Solution()
        assert (
            sc.validIPAddress(
                queryIP,
            )
            == output
        )
