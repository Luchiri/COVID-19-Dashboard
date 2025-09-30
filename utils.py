import pycountry

def country_name_to_iso3(name: str):
    """Return ISO3 code for a country name, or None if not found."""
    try:
        return pycountry.countries.lookup(name).alpha_3
    except Exception:
        return None
