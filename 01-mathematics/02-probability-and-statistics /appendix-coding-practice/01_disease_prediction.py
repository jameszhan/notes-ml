#coding=utf-8


def bayes(pT, pfT, pf_T):
    return (pfT * pT) / (pfT * pT + pf_T * (1 - pT))


# P(T)
pT = 0.0001
# P(f|T)
pfT = 0.999
# P(f|-T)
pf_T = 0.0001

ret = bayes(pT, pfT, pf_T)
print("First Bayes: ", ret)

print("Second Bayes: ", bayes(ret, pfT, pf_T))