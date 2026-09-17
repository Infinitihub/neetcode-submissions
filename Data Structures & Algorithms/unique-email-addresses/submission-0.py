class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 0
        unique = set()
        for s in emails:
            local, domain = s.split('@')
            local = local.split('+')[0]
            final = ""
            for char in local:
                if char == '.':
                    continue
                final += char
            if final+domain not in unique:
                res += 1
                unique.add(final+domain)
        return res