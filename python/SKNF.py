from browser import document, html, window, alert

def sort_str(s, cnt):
    otr = [0] * (cnt + 1)
    for i in range(1, len(s)):
        if (s[i - 1] == '!'):
            otr[ord(s[i]) - ord('a')] = 1
    ans = ''
    s = ''.join(sorted(s))
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            if otr[ord(s[i]) - ord('a')]:
                ans += '!'
            ans += s[i]
            ans += ' + '
    return '(' + ans[0:-3] + ')'
 
 
def add_one(s, cur):
    s = s[s.find('(') + 1: s.find(')')]
    return '(' + s + " + " + cur + " * !" + cur + ')'
 
 
def close_bracket(s, cur):
    s = s[s.find('(') + 1: s.find(')')]
    s = s[0: len(s) - 9]
    return '({} + {}) * ({} + !{})'.format(s, cur, s, cur)
 
 
def get_component(s,cnt):
    s = '*' + s + '*'
    pos = []
    for i in range(len(s)):
        if s[i] == '*':
            pos.append(i)
    a = []
    for i in range(1, len(pos)):
        l = pos[i - 1]
        r = pos[i]
        cur = s[l: r]
        if '(' not in cur:
            while cur[0] == ' ' or cur[0] == '*':
                cur = cur[1:]
            while cur[-1] == ' ' or cur[-1] == '*':
                cur = cur[:-1]
            cur = '(' + cur + ')'
        cur = cur[cur.find('('): cur.find(')') + 1]
        a.append(sort_str(cur,cnt))
    return a
 
 
def main(s, cnt):
    total = ''
    SKNF = ''
    a = get_component(s,cnt)
 
    for i in a:
        SKNF += i
        SKNF += ' * '
 
    SKNF = SKNF[0:len(SKNF) - 3]
    for add_char in range(0, cnt):
        ch = chr(add_char + ord('a'))
        plus = ''
        pr = ''
        check = 0
        for i in range(len(a)):
            if ch in a[i]:
                plus += a[i]
                plus += ' * '
 
                pr += a[i]
                pr += ' * '
            else:
                a[i] = add_one(a[i], ch)
                plus += a[i]
                plus += ' * '
 
                a[i] = close_bracket(a[i], ch)
                pr += a[i]
                pr += ' * '
 
                check = 1
        plus = plus[0:len(plus) - 3]
        pr = pr[0:len(pr) - 3]
        a = get_component(pr,cnt)
        if check:
            total += "Добавим в множители " + ch + ":\n"
            total += plus + '\n'
            total += pr + '\n'
            SKNF = pr
    return total + "СКНФ : " + SKNF

def senddata(event):
    num = int(document["num_input"].value)
    str = document["str_input"].value
    taera = document["textar"]
    taera.value = main(str, num)
   
document["sendbutton"].bind("click", senddata)