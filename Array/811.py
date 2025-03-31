# 811. Subdomain Visit Count (Mode: Medium)

class Solution(object):
    
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        domain_counts = {}

        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                if subdomain in domain_counts:
                    domain_counts[subdomain] += count
                else:
                    domain_counts[subdomain] = count

        return ["{} {}".format(count, domain) for domain, count in domain_counts.items()]