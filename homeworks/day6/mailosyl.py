import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pogodne_foty import weather_report, pic_from_web_tool


url = "https://wallpaperlist.com"
px = 64
pic_stats = pic_from_web_tool(url, px)
weather = weather_report("800101cc05e0bcd5b88c816246c988ff", "http://api.openweathermap.org/data/2.5/weather", "Gdansk")


subject = input("Podaj temat: ")
body = f"Cześć Łukasz!\nZadanie wykonane. Na stronie {url} znajduje się obecnie {pic_stats[3]} obrazów, udało ściągnąć się {pic_stats[4]} do katalogu \images na moim dysku.\nŁączny rozmiar pobranych obrazów wyniósł {pic_stats[0]} MB. " \
       f"Po ich pomniejszeniu do szerokości {px} pixeli, sumaryczny rozmiar wyniósł {pic_stats[1]} MB, zaoszczędziłem zatem {pic_stats[2]} MB na moim dysku!\n" \
       f"{weather}\nTo by było wszystko. Do zobaczenia na zajęciach."
recipient = input("Podaj adresata: ")

mail_body = MIMEText(body)

mail = MIMEMultipart()
mail["Subject"] = subject
mail["From"] = "isapy_second@interia.pl"
mail["To"] = recipient
mail.attach(mail_body)

server = smtplib.SMTP("poczta.interia.pl")
server.starttls()
server.login("isapy_second@interia.pl", "isapython;")
server.send_message(mail)
server.quit()