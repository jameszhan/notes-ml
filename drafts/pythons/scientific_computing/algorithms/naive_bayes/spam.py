#coding=utf-8

def bayes(pS, pwS, pwH):
    return (pwS * pS) / (pwS * pS + pwH * (1 - pS))


pS = 0.5
pH = 1 - pS
pwS = 250.0 / 5000
pwH = 5.0 / 5000

pSw = bayes(pS, pwS, pwH)
print(pSw)


# P(S,w1,w2) = P(S) * P(w1|S) * P(w2|S,w1)
# Independence hypothesis => P(S,w1,w2) = P(S) * P(w1|S) * P(w2|S)
def joint(pS, pw1S, pw2S):
    return pS * pw1S * pw2S


pw1S = pwS
pw1H = pwH
pw2S = 495.0 / 5000
pw2H = 5.0 / 5000


pE1 = joint(pS, pw1S, pw2S)
pE2 = joint(pH, pw1H, pw2H)

print(pE1)
print(pE2)

# P(S|w1,w2) = P(S,w1,w2) / P(w1,w2)
# = P(E1) / P(w1,w2|S) * P(S) + P(w1,w2|H)*P(H)
# = P(E1) / P(E1) + P(E2)

print(pE1 / (pE1 + pE2))


pSw1 = bayes(pS, pw1S, pw1H)
pSw2 = bayes(pS, pw2S, pw2H)
e1 = pS * pSw1 * pSw2
e2 = pH * (1 - pSw1) * (1 - pSw2)
print(e1 / (e1 + e2))