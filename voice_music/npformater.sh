#!/bin/bash
 
 sed "s/^.*title': '//" /path/to/your/nowplayingraw | sed "s/'}.*//g" > /path/to/your/nowplaying
 #format of nowplayingraw = [{'source':'**url**','title':'**vid_title**'}, <discord info>]
 #this remove everything before and after the vid_title, then outputs to 'nowplaying'
