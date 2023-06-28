import requests as rs     # Call requests library

from bs4 import BeautifulSoup     # Import BeautifulSoup method from bs4 library

import time as t     # Call time library

import threading as th # Call threading library

Start = t.time()     # Take the start time of code

Name = []     # An empty list to get names later

Info_List = []     # A vacant list for getting information later

Price = []     # An empty list for prices

def Get(url):
    
    """ This function get a url, send a request to that url and finally parse it. """
    
    Response = rs.get(url)     # With requests library send a request to url

    Soup = BeautifulSoup(Response.text , "html.parser")
    
    # Using BeautifulSoup method to get all page source code and parse it with html.parser method
    
    return Soup
    
def Information(I):
    
    """ This function put laptop names and information onto lists mentioned above. """
    
    Product_Info = I.select_one("div.OfferBoxProdInfo")
    
    # Using select_one method to get an specefic tag name with a special class in source code and name it Product_Info
    
    Details = Product_Info.select_one("div.productInfo")
    
    Name.append(Product_Info.select_one("a").text)
    
    # Putting Product_Info contents with select_one on tag name "a" into Name list
    
    Rows = Details.select("li")     # Find all "li" tag names

    for Row in Rows:
        
        Info_List.append(Row.text)
        
    # The loop above put contents of Rows list onto Info_List
    
def Price_Function(P):
    
    """ This function put laptop prices into Price list. """
    
    Pri = P.select_one("div.OfferBoxPrice")     # Using select_one method find the first div tag with "OfferBoxPrice" class
            
    Price.append(float(Pri.select_one("span.offerprice").text.strip().replace("£" , "")))

for Page in range(1 , 20):
    
    """ The loop above with url below search in 19 pages. """
    
    Parsed = Get(f"https://www.laptopsdirect.co.uk/c/phones?pageNumber={Page}")  # Call Get function
        
    Products = Parsed.select_one("div#products")
    
    # Select everything within tag name div and "products" id and returns a list
        
    for Element in Products.select("div.OfferBox"):
        
        Thread_Information = th.Thread(target = Information , args = (Element , ))
        
        Thread_Price = th.Thread(target = Price_Function , args = (Element , ))
        
        Thread_Information.start()
        
        Thread_Information.join()

        Thread_Price.start()

        Thread_Price.join()
            
for i in range(len(Name)):
    
    print(f"Mobile Phone{i + 1}:\n")
    
    print(f"\tName: {Name[i]}\n")
    
    print("\tInformation:\n")
    
    [print(f"\t\t{Info_List[4 * i + j]}\n") for j in range(4)]
        
    print(f"\tPrice: £{Price[i]}\n")
    
    print(120  * "-")
    
Max = max(Price)

Min = min(Price)

print(f"Mobile Phone with highest price: {Name[Price.index(Max)]}\n")

print(f"Mobile Phone with lowest price: {Name[Price.index(Min)]}\n")

print(f"Highest price: £{Max}\n")

print(f"lowest price: £{Min}\n")

print(f"Average price: £{sum(Price) / len(Price)}\n")

End = t.time()

print(f"{End - Start} seconds elapsed!")
