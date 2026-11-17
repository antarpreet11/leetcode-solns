# Time - O(n), Space - O(n), n = unique domains
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        subdomainDict = defaultdict(int)

        for cpd in cpdomains:
            count, domain = cpd.split(" ")
            count = int(count)

            subdomainDict[domain] += count
            
            while "." in domain:
                dot = domain.find(".")
                domain = domain[dot+1:]
                subdomainDict[domain] += count

        return [f'{count} {domain}' for domain, count in subdomainDict.items()]