products = {"Leather Wallet":1100,"Umbrella": 900,"Clgarette": 200,"Honey": 100}
GST = [18, 12, 28, 0]
quantity = [1, 4, 3, 2]
pc={}
total_amount = 0
j = 0
for i in products:
    pa = products[i] * quantity[j] 
    if products[i] > 500:
        discount = pa * 0.05
        pa = pa - discount
    gst = pa * (GST[j]/100)
    ps = pa + gst
    total_amount+=ps
    pc[i]=gst
    j+=1

# Find the maximum amount of GST paid among the products
max_gst_p = max(pc, key=pc.get)
max_gst = pc[max_gst_p]

print("Maximum GST paid for the product {max_gst_p} that is {max_gst}".format(max_gst_p=max_gst_p,max_gst=max_gst))
print("Total Amount paid to Shopkeeper:", total_amount)
