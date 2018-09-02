width = 20
print("ljust")
print 'H'.ljust(width,'-')
print 'H'.ljust(19,'-')
print 'H'.ljust(18,'-')
print 'H'.ljust(17,'-')
print 'H'.ljust(16,'-')
print(' ')
# HackerRank----------

print("center")
print 'H'.center(width,'-')
print 'H'.center(19,'-')
print 'H'.center(18,'-')
print 'H'.center(17,'-')
print 'H'.center(16,'-')

print(' ')
print("rjust")
# -----HackerRank-----
print 'H'.rjust(width,'-')
print 'H'.rjust(19,'-')
print 'H'.rjust(18,'-')
print 'H'.rjust(17,'-')
print 'H'.rjust(16,'-')

print(' ')
print(' ')
print(' ')
print(' ')

#Replace all ______ with rjust, ljust or center.
# thickness = int(input()) #This must be an odd number
ep = 5
c = 'H'

# #Top Cone
for i in range(ep):

    print((c*i).rjust(ep-1)+c+(c*i).ljust(ep-1))
#
# #Top Pillars
for i in range(ep+1):
    print((c*ep).center(ep*2)+(c*ep).center(ep*6))
#
# #Middle Belt
for i in range((ep+1)//2):
    print((c*ep*5).center(ep*6))
#
# #Bottom Pillars
for i in range(ep+1):
    print((c*ep).center(ep*2)+(c*ep).center(ep*6))
#
# #Bottom Cone
for i in range(ep):
    print(((c*(ep-i-1)).rjust(ep) +  c + (c*(ep-i-1)).ljust(ep)).rjust(ep*6))
