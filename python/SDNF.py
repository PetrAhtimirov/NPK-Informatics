from browser import document, html, window, alert

def sort_str(s, cnt):
    otr = [0] * (cnt + 1)
    for i in range(1, len(s)):
        if (s[i - 1] == '!'):
            otr[ord(s[i]) - ord('a')] = 1
    ans = ''
    s = ''.join(sorted(s))
    for i in s:
        if (i == '!'):
            continue
        x = ord(i)
        if (otr[x - ord('a')]):
            ans += '!'
        ans += i
    return ans
 
 
def add_one(s, cur):
    add = ''
    add += '('
    add += cur
    add += " + "
    add += '!'
    add += cur
    add += ')'
    return s + add
 
 
def open_bracket(s):
    cur = s[s.find('(') + 1]
    left = s[0:s.find('(')] + cur
    right = s[0:s.find('(')] + '!' + cur
    return left + ' + ' + right
 
 
def get_component(s, cnt):
    s += '+'
    a = []
    cur = ''
    for i in s:
        if i == '+':
            cur = sort_str(cur, cnt)
            a.append(cur)
            cur = ''
        else:
            if i != ' ':
                cur += i
    return a
 
 
def main(s, cnt):
    total = ''
    SDNF = ''
    a = get_component(s, cnt)
    for i in a:
        SDNF += i
        SDNF += ' + '
    SDNF = SDNF[0:len(SDNF) - 3]
    for i in range(0, cnt):
        ans_closed_bracket = ''
        ans_opened_bracket = ''
        check = 0
        for j in range(len(a)):
            ch = chr(i + ord('a'))
            if ch not in a[j]:
                a[j] = add_one(a[j], ch)
 
                ans_closed_bracket += a[j]
                ans_closed_bracket += " + "
 
                a[j] = open_bracket(a[j])
 
                ans_opened_bracket += a[j]
                ans_opened_bracket += " + "
 
                check += 1
            else:
                ans_closed_bracket += a[j]
                ans_closed_bracket += " + "
 
                ans_opened_bracket += a[j]
                ans_opened_bracket += " + "
        ans_opened_bracket = ans_opened_bracket[0:len(ans_opened_bracket) - 3]
        ans_closed_bracket = ans_closed_bracket[0:len(ans_closed_bracket) - 3]
        a = get_component(ans_opened_bracket, cnt)
        if check:
            total += "Добавляем "
            total += chr(i + ord('a'))
            total += " в слагаемые\n"
            total += ans_closed_bracket
            total += "\n"
            total += ans_opened_bracket
            total += "\n"
            SDNF = ans_opened_bracket
    total += "СДНФ : "
    total += SDNF
    return total

def senddata(event):
    num = int(document["num_input"].value)
    str = document["str_input"].value
    taera = document["textar"]
    taera.value = main(str, num)
   
document["sendbutton"].bind("click", senddata)
