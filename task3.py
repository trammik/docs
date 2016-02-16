def addAndMultiply(digs):
    if len(digs) == 0:
        res=0
    else:
        res=sum(digs[::2])*digs[len(digs)-1]
    return 'Add and multiplying of list %s == %s ' % (digs,res)

print addAndMultiply([0, 1, 2, 3, 4, 5])
print addAndMultiply([1, 3, 5])
print addAndMultiply([6])
print addAndMultiply([])
