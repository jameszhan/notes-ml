

def bayes(pT, pfT, pf_T):
    return (pfT * pT) / (pfT * pT + pf_T * (1 - pT))


# P(T)
pT = 0.0001
# P(f|T)
pfT = 0.999
# P(f|-T)
pf_T = 0.0001

ret = bayes(pT, pfT, pf_T)
print ret

print bayes(0.49977, pfT, pf_T)

print 1.0/10000 + 0.999