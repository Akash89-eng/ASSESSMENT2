transcation=[
  ("101","Deposit",5000),
  ("102","Deposit",15000),
  ("103","Withdrawal",2000),
  ("104","Deposit",25000),
  ("105","Withdrawal",12000)
]
balance={}
dep=wd=0
for accc,t,amt in transcations:
  balance.setdefault(acc, 0)
  if t == "Deposit":
    balance[acc] += amt
    dep+=amt
  else:
    balance[acc] -= amt
    wd+=amt
    if amt >10000:
      print("Suspicious: " , acc, amt)

print("Total deposit =", dep)
print("Total Withdrawl =", wd)
print("Highest balance =",max(balance,key=balance.get), balance[max(balance,key=balance.get)])
print("Finanl Balance =",balance)
