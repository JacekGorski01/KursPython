from PIL import Image
from bs4 import BeautifulSoup
from conversion import KtoC
import requests
import os

# image = Image.open('/home/master/Pictures/index.jpeg')
# image = image.resize((400,400))
# image.save("/home/master/Pictures/index-2.jpeg")
# image = image.rotate(90)
# #image.show()


def weather_report(api_key, api_host, city):
    # api_key = '800101cc05e0bcd5b88c816246c988ff'
    # api_host = 'http://api.openweathermap.org/data/2.5/weather'
    # city = 'Gdansk'

    result = requests.get(f'{api_host}?appid={api_key}&q={city}')
    dict = result.json()
    temp = KtoC((dict['main']['temp']))
    weather = (f"\nPogoda w {city}u przestawia się tak: temperatura: {temp} \u2103, wiatr: {dict['wind']['speed']} m/s. \n")

    return weather


def pic_from_web_tool(page, conv_to_size):
    page = requests.get('https://wallpaperlist.com')
    parser = BeautifulSoup(page.content, 'html.parser')
    images = parser.find_all('img')
    img_count = len(images)

    size_before = 0
    size_after = 0
    img_count_downloaded = 0

    for i, image in enumerate(images):
        url = 'https://wallpaperlist.com' + (image['src']) #montuje pełen url do obrazu na image'src' to ścieżka
        pic_name = url.split('/')[-1] #rozdziela url na listę stringów i pokazuje ostatni, który jest nazwą obrazu

        picture = requests.get(url)


        if picture.status_code == 200:
            with open(f"/home/master/Pictures/images/{pic_name}", 'wb') as x:
                x.write(picture.content)
                img_count_downloaded += 1

        image = Image.open(f'/home/master/Pictures/images/{pic_name}')
        width, height = image.size
        size_before = (os.stat(f'/home/master/Pictures/images/{pic_name}').st_size) + size_before # sumowanie do zmiennej łącznej wagi obrazu przed resizem
        image = image.resize((conv_to_size,(int(height / (width / conv_to_size))))) # resize obrazu na szer 64px i wysokość proop. wg ratio wys przez iloraz szerokości przez 64

        image.save(f'/home/master/Pictures/images/{pic_name}', quality=100, optimize=True)
        size_after = os.stat(f'/home/master/Pictures/images/{pic_name}').st_size + size_after


    size_before = size_before / 10 ** 6
    size_after = size_after / 10 ** 6
    total_size_diff = size_before - size_after


    return size_before, size_before, total_size_diff, img_count, img_count_downloaded


