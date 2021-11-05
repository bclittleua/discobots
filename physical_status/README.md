This bot requires a PIR motion sensor and Rpi with a breakout board and has a few moving parts. 
- desk_alert.py controls the PIR and occasionally writes a status to a new file, 'flag'.
- - flag = 1 if motion has been triggered, flag = 0 if PIR is idle
- aqui_bot.py is a discord bot that simply runs a task loop and checks 'flag'
- - if flag = 0 then bot status is set to DND/Red
- - if flag = 1 then bot status is set to Online/Green
