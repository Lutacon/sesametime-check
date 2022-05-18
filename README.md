Easy tool to check in and check out in [SesameTime](https://www.sesametime.com/es/) app.

## Requirements
 - [chromedriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver#quick-installation) 

## Usage
```
# First install python requirements.
pip3 install -r requirements.txt

# For check in
./sesame.py --action in
# For checkout
./sesame.py --action out 
```

You should set up a cronjob to forget about it
```
# m h  dom mon dow   command
55 8 * * 1-5 ./sesame.py --action in
55 17 * * 1-5 ./sesame.py --action out
```

## Credits

It's based(aka copied) on [AlexLoar](https://github.com/AlexLoar/woffu-less) app [woffu-less](https://github.com/AlexLoar/woffu-less).
