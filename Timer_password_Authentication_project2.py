# importing sleep from time module
from time import sleep

#lets set a unique password
password = "123@2023"

#initial number of trials = 5
trials = 5

#lets loop it
while True:

  # lets take input from the user for password
  user_password = input('please Enter your password: ')

  # lets Compare both the password
  if password != user_password:

    # Reduce the by value by 1
    trials = trials - 1

    # if this the last traial
    if trials == 0:

      # print counting for 30 seconds
      # the phone has to remain locked for 30 second
      counting = 30
      while True:
        print('Phone is locked', counting, 'seconds')
        counting = counting - 1
        if counting == 0:
          trials = 5
          break
        sleep(1)
        
    print('Wrong pasword', trials, "trials left")

  else: 
    print('Welcome prince')
    break
