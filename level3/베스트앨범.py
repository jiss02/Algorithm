from collections import defaultdict

def solution(genres, plays):
    answer = []
    eachGenres = defaultdict(list)
    genresSum = defaultdict(int)
    for genre, play, i in zip(genres, plays, range(0,len(genres))):
        genresSum[genre] += play
        eachGenres[genre].append((play, i))
    best = sorted(genresSum.items(), key=lambda x:x[1], reverse=True)
    for genre, num in best:
        top2 = sorted(eachGenres[genre], key=lambda x:x[0], reverse=True)[:2]
        answer.append([i[1] for i in top2])
    return sum(answer,[])