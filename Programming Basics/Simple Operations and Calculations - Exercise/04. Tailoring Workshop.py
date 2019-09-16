number_of_tables = int(input())
lenght_of_tables = float(input())
width_of_tables = float(input())

price_of_cover = 7
price_of_square = 9

total_area_of_cover = number_of_tables * (lenght_of_tables + 2 * 0.3) * (width_of_tables + 2 * 0.3)
total_area_of_square = number_of_tables*(lenght_of_tables / 2) * (lenght_of_tables / 2)
usd_total_price = total_area_of_cover * price_of_cover + total_area_of_square * price_of_square
bgn_price = usd_total_price * 1.85
print(f"{usd_total_price:.2f} USD")
print(f"{bgn_price:.2f} BGN")