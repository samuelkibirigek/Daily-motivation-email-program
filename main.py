import datetime as dt
import smtplib
import random

final_quote_list = []
now = dt.datetime.now()
working_days = [0, 1, 2, 3, 4]
if now.weekday() in working_days:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        for quote in quotes_list:
            clean_quote = quote.strip("\n")
            final_quote_list.append(clean_quote)

    random_quote = random.choice(final_quote_list)

    with open("email_listing.txt") as emails:
        for email in emails.readlines():
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user="kibirigekalules@gmail.com", password="my_password")
                connection.sendmail(
                    from_addr="kibirigekalules@gmail.com",
                    to_addrs=f"{email}",
                    msg=f"Subject:Quote of the day\r\n{random_quote}\r\r\nKind Regards,\r\nSamuel KK."
                )
