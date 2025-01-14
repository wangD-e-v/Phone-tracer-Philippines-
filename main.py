import phonenumbers
from phonenumbers import geocoder, carrier

# Enter your phone number
phone_number = phonenumbers.parse("+639462494191", "PH")  # Replace XXXXXXXXX with your actual phone number

# Get location (e.g., region or city)
location = geocoder.description_for_number(phone_number, "en")

# Get the carrier (e.g., Globe, Smart)
service_provider = carrier.name_for_number(phone_number, "en")

# Display results
print(f"Phone Number: {phone_number}")
print(f"Location: {location}")
print(f"Carrier: {service_provider}")
