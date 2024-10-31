def feet_to_steps(user_feet):
   return(int(user_feet/2.5))

if __name__ == '__main__':
    #taek input feet steps here
    user_feet=float(input())
    #store it into the function
    steps=feet_to_steps(user_feet)
    #print your steps here
    print(steps)
    feet_to_steps(5280)