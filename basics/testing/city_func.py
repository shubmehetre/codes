def city_country(city, country, pop=''):
    if pop:
        ans = f"{city}, {country}, population = {pop}"
    else:
        ans = f"{city}, {country}"

    return ans.title()

