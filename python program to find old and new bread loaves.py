new_count=int(input("enter the number of new loaves purchased:"))
old_count=int(input("enter the number of old loaves purchased:"))
rate_old=(185-(0.6*185))*old_count
rate_new=185*new_count
print("Regular Price:Rs.185")
print("Amount of new loaves :Rs.",rate_new)
print("Amount of old loaves :Rs.",rate_old)
print("Total Amount:Rs.",rate_old+rate_new)
