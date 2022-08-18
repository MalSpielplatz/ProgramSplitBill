print("--------------Program Split Bill--------------")
bill = int(input("berapa total nya? Rp."))
tip = float(input("mau kasih tips berapa persen? "))
man = int(input("berapa jumlah orang yang akan membayar ? "))

tip_formula = tip / 100
hasil_total_tip = bill * tip_formula  
harus_dibayar = hasil_total_tip + bill
split_bill = harus_dibayar / man


print(f"jadi total yang harus dibayar adalah Rp. {harus_dibayar} dan setiap orang harus membayar sebesar Rp.{split_bill} ")
