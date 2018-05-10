## CAT 02Saver API

This a backend for our hack solution for Melbourne Facebook Hackathon 2018

### Getting Started
#### Prerequisites
- Make sure you have `python >= 3.5`
- Make sure you have [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation/) and [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)


#### Running The App
This step by step assume you have all of prerequisites stack above 
- Create new virtual environment
```commandline
$ mkvirtualenv cat02saver --python=python3
```

- Install the dependencies
```commandline
$ pip install -r requirements.txt
```

- Run the `flask app`
```commandline
$ export FLASK_APP=app.py
$ flask run
```

- You can access your api from `http://localhost:5000`

#### Available Route
- POST
  - Get suggestion from image
    
    [http://localhost:5000/vision](http://localhost:5000/vision)
    - You need to pass an image in the `form-body`
    
    Example Request:
    ```commandline
    curl -X POST \
    http://localhost:5000/vision \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'Postman-Token: 18914aa5-8134-4d5b-a2a2-6aad344e8e81' \
    -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
    -F 'image=@<folder>\test_image.jpg'
    ```
    
    Example Response:
    ```json
    {
    "caption": "a glass of beer",
    "data": {
            "CO2 produced": "134.4g",
            "Eco-friendly level": "Low",
            "Landfill": "200-500 years",
            "Suggestions": {
                "Recycle": {
                    "cats": 2,
                    "image": "https://www.canmaker.com/online/file/2016/12/recycling-cans.png",
                    "price": "Free",
                    "text": "Most cans are completely recyclable"
                },
                "Reduce": {
                    "cats": 3,
                    "image": "https://www.gallagheruniform.com/wp-content/uploads/2014/07/Gallager-Reduce-Icon.png",
                    "price": "Free",
                    "text": "Try to avoid single-serve cans."
                },
                "Refuse": {
                    "cats": 5,
                    "image": "http://www.europeancuisines.com/images/aluminum-free.jpg",
                    "price": "Free",
                    "text": "Aluminum cans can take hundreds of years to biodegrade in a landfill."
                },
                "Repurpose": {
                    "option 1": {
                        "cats": 4,
                        "image": "https://oneamanyr.files.wordpress.com/2013/05/2670f8180805bade7e99592a5249a217.jpg",
                        "price": "Free",
                        "text": "Make a bird feeder out of used cans."
                    }
                }
            },
            "isEcoFriendly": 0
        },
        "product": "Aluminum Can"
    }
    ```
  
