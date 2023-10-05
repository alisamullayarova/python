dom = input()
out = ''
while 1:
    if len(dom) > 0:
        st = dom[0]
        if st!= '.':
            out += st
            dom = dom[1::]
        else:
            print(otv)
            dom = dom[1::]
            out = ''
    else:
        print(out)
        break
        
