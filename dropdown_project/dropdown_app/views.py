from django.shortcuts import render

IMAGES = {
    "fruits": {
        "apple": "https://images.pexels.com/photos/588587/pexels-photo-588587.jpeg?cs=srgb&dl=apple-blur-bright-588587.jpg&fm=jpg",
        "banana": "https://purepng.com/public/uploads/large/purepng.com-bananafruitsyellowfruit-981524754330lspp8.png",
        "orange": "https://wallpapercave.com/wp/wp2293578.jpg"
    },
    "cars": {
        "bmw": "https://wallsdesk.com/wp-content/uploads/2016/05/BMW-I8-Wallpapers-HD.jpg",
        "audi": "https://s3.paultan.org/image/2018/11/Audi-e-tron-GT-concept-22-e1555984783556.jpg",
        "tesla": "http://www.hdcarwallpapers.com/walls/tesla_roadster_sports_car-wide.jpg"
    }
}

def index(request):
    return render(request, 'index.html', {"images": IMAGES})

def item_detail(request, category, item_name):
    image_url = IMAGES.get(category, {}).get(item_name)
    if not image_url:
        image_url = "https://via.placeholder.com/300x200.png?text=Not+Found"
    return render(request, 'detail.html', {"item": item_name, "image_url": image_url})