import datetime as dt
import smtplib
import random

final_quote_list = []
now = dt.datetime.now()
if now.weekday() == 1:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        for quote in quotes_list:
            clean_quote = quote.strip("\n")
            final_quote_list.append(clean_quote)

    random_quote = random.choice(final_quote_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="leumaselulakk@gmail.com", password="the_password:)")
        connection.sendmail(
            from_addr="leumaselulakk@gmail.com",
            to_addrs="samuelkibirigek@gmail.com",
            msg=f"Subject:Quote of the day\n\n{random_quote}"
        )

