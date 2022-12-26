import accounts, buyers, lots_of_goods, names_of_techniques, sales, technics

routers = (accounts.accounts_router, buyers.buyers_router, lots_of_goods.lots_of_goods_router,
           names_of_techniques.name_technics_router, sales.sales_router, technics.technics_router)
