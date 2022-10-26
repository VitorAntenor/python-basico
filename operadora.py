import phonenumbers
from phonenumbers import geocoder, carrier

phoneNumer = phonenumbers.parse("+5532*********")

Carrier = carrier.name_for_number(phoneNumer, 'pt-br')

Region = geocoder.description_for_number(phoneNumer, 'pt-br')

print("Operadora: " + Carrier)
print("Estado: " + Region)