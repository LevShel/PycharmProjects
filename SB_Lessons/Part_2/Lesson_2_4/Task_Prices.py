def get_higer_price(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]

print('Prices now: ', prices_now)
x = int(input('1st price increase in %: '))
y = int(input('2nd price increase in %: '))

prices_x = [get_higer_price(x,i) for i in prices_now]
prices_y = [get_higer_price(y,i) for i in prices_x]

print('Sum of prices for each year:\n', round(sum(prices_now),2), '\n', round(sum(prices_x),2), '\n',round(sum(prices_y),2))