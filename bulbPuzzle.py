# you have 3 light bulbs in a room on first floor
# 3 switches on these bulbs are on ground floor
# You can press switches as many number of times you want
# But you allow only 1 time to go room where bulbs are to check
# tell which switch is for which bulb?

#solution:
# open 1st switch for 1 min and then off - bulb connected to this switch must be hot
# open 2nd switch - bulb connected to this switch must be hot

def bulb_to_switch(bulb, inp):
    if inp == 'hot':
        ans = '%s belongs to switch 1' % bulb
    elif inp == 'cold':
        ans = '%s belongs to switch 3' % bulb
    elif inp == 'lit':
        ans = '%s belongs to switch 2' % bulb
    else:
        print 'Please choose from hot, cold and lit only'
        inp = raw_input('What is the status of %s ? options are: hot, cold or lit' % bulb)
        bulb_to_switch(bulb, inp)
    return ans

print 'come to ground floor where switches are located'
raw_input('press enter if you can see 3 switches?')

print 'Turn on 1st switch for 2 mins and then turn off'
raw_input('press enter after you turn off switch')

print 'Turn on 2nd switch and go to first floor to see the switches'
raw_input('press enter when you can see bulbs')

print 'Touch bulb 1 and follow instruction'
bulb1_inp = raw_input('What is the status of bulb1? options are: hot, cold or lit?')
bulb1_ans = bulb_to_switch('bulb1', bulb1_inp)

print 'Touch bulb 2 and follow instruction'
bulb2_inp = raw_input('What is the status of bulb2? options are: hot, cold or lit?')
bulb2_ans = bulb_to_switch('bulb2', bulb2_inp)

print 'Touch bulb 3 and follow instruction'
bulb3_inp = raw_input('What is the status of bulb3? options are: hot, cold or lit?')
bulb3_ans = bulb_to_switch('bulb3', bulb3_inp)

print 'All done! Solution to the puzzle is:'
print '%s \n%s \n%s' % (bulb1_ans, bulb2_ans, bulb3_ans)
