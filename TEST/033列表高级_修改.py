city_list = ['beijing','shanghai','shenzhen','wuhan','xian']
print(city_list)
city_list[4] = 'dalian'
print(city_list)
'''
if 's' in city_list:
    print('1')
else:
    print('2')
'''
city_list.remove('beijing')
print(city_list)