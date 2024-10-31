def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   return(dollars_per_gallon*miles_driven/miles_per_gallon)

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    cost_to_miles=driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    print(f'{cost_to_miles:.2f}')
    cost_to_miles=driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    print(f'{cost_to_miles:.2f}')
    cost_to_miles=driving_cost(miles_per_gallon, dollars_per_gallon, 400)
    print(f'{cost_to_miles:.2f}')