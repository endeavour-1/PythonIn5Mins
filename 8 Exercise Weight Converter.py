Weight = input("Weight: ")
Metric = input("(K)g or (L)bs: ")
if Metric.upper == "K":
    converted = float(Weight) / 0.45
    print("Weight in (L)bs: " + str(converted))
else:
    converted = float(Weight)*(0.45)
    print("Weight in (K)g:" + str(converted))


