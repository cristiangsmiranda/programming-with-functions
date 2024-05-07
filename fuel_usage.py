
def main():
        
    start_miles = int(input("Enter the first odometer reading (miles): "))
    end_miles = int(input("Enter the second odometer reading (miles): "))
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon (start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg (mpg)

    print (f" {mpg:.2f} miles per gallon ")
    print (f" {lp100k:.2f} liters per 100 kilometers")
    
def miles_per_gallon(start_miles, end_miles, amount_gallons):

    mpg = (end_miles - start_miles) / amount_gallons
    return mpg
    
def lp100k_from_mpg(mpg):
    
    lp100k = 235.215 / mpg
    return lp100k
    
main()