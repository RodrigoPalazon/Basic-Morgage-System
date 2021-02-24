housePrice = float(input('What\'s the house\'s price? $'))
salary = float(input('What\'s your salary? $'))
installments = int(input('In how many years would you like to pay this house?'))

mounths = installments * 12
instPrice = housePrice / mounths
maxPay = salary * 30 / 100

if instPrice > maxPay:
    print('You CANNOT pay {}{:.2f}{} monthly for {}{}{} years'.format('\033[33m', instPrice, '\033[m', '\033[36m', installments, '\033[m'))
else:
    print('You will pay {}{:.2f}{} monthly for {}{}{} years'.format('\033[33m', instPrice, '\033[m', '\033[36m', installments, '\033[m'))



