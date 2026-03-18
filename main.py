def orders_consult(orders):
    #Initialize Variables
    userOrder = {}
    AllProductsTotal = 0
    #User CC for searching orders
    clientIdentification = input("\nEnter the client's CC: ")
    
    #Accesing every order in orders dictionary 
    for i, order in orders.items():
        #Validation if the user have made any orders
        if clientIdentification == order["client_id"]:
            #Dictionary with all the products of the user
            userOrder[i] = order.get("products") #Contains the products within a tuple

            #Show the user the summary of their orders
            print(f"\n-----Order Summary-----\nClient Identification: {clientIdentification}\nProducts:")
            #Accesing the user order
            for i, product in userOrder.items():
                totalIndividualProducts = product[1]*product[2] #The total for the individual product and its quantity (E.g. Soap x quantity of soap)
                print(f"Name: {product[0]}; Price: ${product[1]}; Quantity: x{product[2]}; The Product Total: ${totalIndividualProducts}")
            AllProductsTotal += totalIndividualProducts #The total for all the products the user have ordered 
            print(f"--> All Products Total: {AllProductsTotal}")
        else:
            print("\nThe user have not made any orders")
    
orders_consult(orders)