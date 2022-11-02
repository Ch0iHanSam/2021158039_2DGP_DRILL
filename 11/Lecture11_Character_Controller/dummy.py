table = {
    "SLEEP" : {'HIT' : 'WAKE'},
    "WAKE" : {'HIT : SLEEP'}
}

event = 'HIT'
cur_state = "SLEEP"
print(table[cur_state]['HIT'])
print(table['WAKE']['TIMER10'])