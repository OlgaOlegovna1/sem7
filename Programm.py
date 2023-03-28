from Product import*
from Vending_Machine import*
from Cold_Drinks import*
from Snack import*

cold_drink1 = Cold_Drinks("pepsi",100,0.5)
cold_drink2 = Cold_Drinks('fanta',110,0.5)
cold_drink3 = Cold_Drinks('cola',150,0.6)
cold_drink4 = Cold_Drinks('water',50,0.4)
vm1 = Vending_Machine()
vm1.add_product(cold_drink1)
vm1.add_product(cold_drink2)
vm1.add_product(cold_drink3)
vm1.add_product(cold_drink4)
vm1.get_all_products_cheaper_that(105)

vm2 = Vending_Machine()
snack1 = Snack('peanuts',150,120)
snack2 = Snack('twix',50,40)
snack3 = Snack('cheaps',150,200)
vm2.add_product(snack1)
vm2.add_product(snack2)
vm2.add_product(snack3)
vm2.get_all_products_cheaper_that(100)

vm2.get_product_by_name_price('twix',30)
