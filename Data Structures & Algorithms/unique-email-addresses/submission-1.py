# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         res = 0
#         unique = set()
#         for s in emails:
#             local, domain = s.split('@')
#             local = local.split('+')[0]
#             final = ""
#             for char in local:
#                 if char == '.':
#                     continue
#                 final += char
#             if final+domain not in unique:
#                 res += 1
#                 unique.add(final+domain)
#         return res

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # ignore all dots in the gmail before the @

        # drop the @gmail.com part

        # ignore the p

        mapp = {}
        for email in emails:
            emailsplit = email.split("@")
            email = emailsplit[0]
            domain = emailsplit[1]
            email = email.replace(".", "")
            email = email.split("+")[0]
            email = email + domain

            if email not in mapp:
                mapp[email] = 0
        return len(mapp)

