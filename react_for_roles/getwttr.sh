#!/bin/bash

sudo curl wttr.in/Dallas?format="%l+now:+%t+Sunrise:+%S+Sunset:+%s\n"|sudo tee /path/to/your/weather.txt
##################^replace with your own city
