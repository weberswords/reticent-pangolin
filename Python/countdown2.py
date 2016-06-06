# coding: utf-8

import ui, datetime, time, clipboard, math

def button_tapped(sender):
	'@type sender: ui.Button'

	label = sender.superview['Text_Out']
	goal = datetime.date(2016, 6, 2)
	today = datetime.date.today()
	diff = goal - today

	cal_days=diff.days
	weeks = round(cal_days/7.0)
	
	t_days = cal_days-1-(weeks*2.0)
	t_days = float(t_days)
	kid_days = t_days-2.5
	
	label.text="Including today, there are %d calendar days, %.1f kid days, and %d teacher days left in the school year." % (cal_days, round(kid_days, 2), t_days)
	clipboard.set(label.text)

v = ui.load_view('Countdown2').present('sheet')
