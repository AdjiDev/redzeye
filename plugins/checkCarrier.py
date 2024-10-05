import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import json
def LookupCarrier(phone):
    try:
        parsed_number = phonenumbers.parse(str(phone), None)
        default_region = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)
        phone_info = {
            "creator": "adjisan",
            "status": "Success",
            "Location": location,
            "Region Code": default_region,
            "Timezone": timezoneF,
            "Operator": jenis_provider,
            "Valid Number": is_valid_number,
            "Possible Number": is_possible_number,
            "International Format": formatted_number,
            "Mobile Format": formatted_number_for_mobile,
            "Original Number": parsed_number.national_number,
            "E164 Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "Country Code": parsed_number.country_code,
            "Local Number": parsed_number.national_number
        }
        return json.dumps(phone_info, indent=4)
    except phonenumbers.NumberParseException as e:
        return json.dumps({"error": str(e)}, indent=4)