# -*- coding: utf-8 -*-
def inventory_turnover(year, inventory, cost_of_sales):
    print(f"{year}년 재고자산 회전율 :{round(cost_of_sales/inventory, 2)}")
    return round(cost_of_sales/inventory, 2)

print("=== 재고자산 회전율 ===")
inventory_turnover(2021, 13722, 397290)
inventory_turnover(2020, 13337, 345113)
inventory_turnover(2019, 6147, 283975)
print("======================")
