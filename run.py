from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    bot.set_currency(currency="CAD")
    bot.select_destination('Brest')
    bot.check_dates("2022-04-16", "2022-04-29")
    bot.number_of_adults(adults=3)
    bot.search_of_variants()
    bot.quit()
