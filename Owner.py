import Employee

class Owner(Employee):

    def generateSalesReport(self):
        print("Now Viewing Latest Sales Report")

    def viewProduct(self,productID):
        print("Now Viewing Product Details of ",productID)

    def inventoryReport(self):
        print("Now Viewing Latest Inventory Report")