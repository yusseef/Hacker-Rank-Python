
def timeconvert(s):
    Slice = s[-2:]
    
    if Slice =='PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    if Slice == 'AM' and s[:2] == '12':
        s = '00' + s[2:]

    return (s[:-2])


