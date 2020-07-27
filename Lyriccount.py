def word_count(song):
    song=song.split()
    dic={}
    for word in song:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
    return dic
song=str(input("Enter a sentence"))
print(word_count(song))


