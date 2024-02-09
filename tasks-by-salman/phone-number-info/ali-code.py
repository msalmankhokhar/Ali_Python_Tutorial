from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter your phone number = ")
phone = phonenumbers.parse(number)
time1 = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

print("The Timezone is " , time1)
print("The  Network of this number is ", car)
print("The Country is ", reg)