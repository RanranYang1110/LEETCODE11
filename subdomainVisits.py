#-*- coding:utf-8 -*-
# @author: qianli
# @file: subdomainVisits.py
# @time: 2019/11/10
import collections
def subdomainVisits(cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count
    print(ans)
    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]

cp = ["9001 scholar.google.com"]
print(subdomainVisits(cp))
