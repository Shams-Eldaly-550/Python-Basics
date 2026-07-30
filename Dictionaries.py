convert_month = {
    'Jan' : True ,
    'Feb' : 2 ,
    'Mar' : 3
}
print(convert_month.get('Feb', 'the value does not exist'))
print(convert_month['Jan'])


