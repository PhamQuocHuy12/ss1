def freq(s):
    freq=[]
    for i in s :
        if [i] not in freq:
            freq.insert(-0, [i])
    for letter in freq:
        count = 0
        for j in s:
            if letter[0] == j:
                count +=1
        letter.insert(-1, count)
    freq = sorted(freq, key =lambda x: x[0])
    while (len(freq)>2):
        temp = [0,""]
        temp[0] += (int(freq[0][0])+ int(freq[1][0]))
        temp[1] += str(str(freq[0][1])+ str(freq[1][1]))
        freq.remove(freq[0])
        freq.remove(freq[0])
        freq.insert(0,temp)
        freq = sorted(freq, key=lambda x: x[0])
    return freq
if __name__ == '__main__':
    s = "aaabbccccddddde"
    print(freq(s))