from k_means_clusterer import k_means


def init_hands():
    hands = {}
    #off-suite
    hands["AA-O"] = 85
    hands["AK-O"] = 66
    hands["AQ-O"] = 65
    hands["AJ-O"] = 65
    hands["AT-O"] = 64
    hands["A9-O"] = 62
    hands["A8-O"] = 61
    hands["A7-O"] = 60
    hands["A6-O"] = 59
    hands["A5-O"] = 60
    hands["A4-O"] = 59
    hands["A3-O"] = 58
    hands["A2-O"] = 57
    hands["KK-O"] = 83
    hands["KQ-O"] = 62
    hands["KJ-O"] = 62
    hands["KT-O"] = 61
    hands["K9-O"] = 59
    hands["K8-O"] = 58
    hands["K7-O"] = 57
    hands["K6-O"] = 56
    hands["K5-O"] = 55
    hands["K4-O"] = 54
    hands["K3-O"] = 54
    hands["K2-O"] = 53
    hands["QQ-O"] = 80
    hands["QJ-O"] = 59
    hands["QT-O"] = 59
    hands["Q9-O"] = 57
    hands["Q8-O"] = 55
    hands["Q7-O"] = 54
    hands["Q6-O"] = 53
    hands["Q5-O"] = 52
    hands["Q4-O"] = 51
    hands["Q3-O"] = 50
    hands["Q2-O"] = 49
    hands["JJ-O"] = 78
    hands["JT-O"] = 57
    hands["J9-O"] = 55
    hands["J8-O"] = 53
    hands["J7-O"] = 52
    hands["J6-O"] = 50
    hands["J5-O"] = 49
    hands["J4-O"] = 48
    hands["J3-O"] = 48
    hands["J2-O"] = 47
    hands["TT-O"] = 75
    hands["T9-O"] = 53
    hands["T8-O"] = 52
    hands["T7-O"] = 50
    hands["T6-O"] = 48
    hands["T5-O"] = 47
    hands["T4-O"] = 46
    hands["T3-O"] = 45
    hands["T2-O"] = 44
    hands["99-O"] = 72
    hands["98-O"] = 50
    hands["97-O"] = 48
    hands["96-O"] = 47
    hands["95-O"] = 45
    hands["94-O"] = 43
    hands["93-O"] = 43
    hands["92-O"] = 42
    hands["88-O"] = 69
    hands["87-O"] = 47
    hands["86-O"] = 46
    hands["85-O"] = 44
    hands["84-O"] = 42
    hands["83-O"] = 40
    hands["82-O"] = 40
    hands["77-O"] = 67
    hands["76-O"] = 45
    hands["75-O"] = 43
    hands["74-O"] = 41
    hands["73-O"] = 39
    hands["72-O"] = 37
    hands["66-O"] = 64
    hands["65-O"] = 43
    hands["64-O"] = 41
    hands["63-O"] = 39
    hands["62-O"] = 37
    hands["55-O"] = 61
    hands["54-O"] = 41
    hands["53-O"] = 39
    hands["52-O"] = 37
    hands["44-O"] = 58
    hands["43-O"] = 38
    hands["42-O"] = 36
    hands["33-O"] = 55
    hands["32-O"] = 35
    hands["22-O"] = 51
    #suited hands
    hands["AK-S"] = 68
    hands["AQ-S"] = 67
    hands["AJ-S"] = 66
    hands["AT-S"] = 65
    hands["A9-S"] = 64
    hands["A8-S"] = 63
    hands["A7-S"] = 63
    hands["A6-S"] = 62
    hands["A5-S"] = 62
    hands["A4-S"] = 61
    hands["A3-S"] = 60
    hands["A2-S"] = 59
    hands["KQ-S"] = 64
    hands["KJ-S"] = 64
    hands["KT-S"] = 63
    hands["K9-S"] = 61
    hands["K8-S"] = 60
    hands["K7-S"] = 59
    hands["K6-S"] = 58
    hands["K5-S"] = 58
    hands["K4-S"] = 57
    hands["K3-S"] = 56
    hands["K2-S"] = 55
    hands["QJ-S"] = 61
    hands["QT-S"] = 61
    hands["Q9-S"] = 59
    hands["Q8-S"] = 58
    hands["Q7-S"] = 56
    hands["Q6-S"] = 55
    hands["Q5-S"] = 55
    hands["Q4-S"] = 54
    hands["Q3-S"] = 53
    hands["Q2-S"] = 52
    hands["JT-S"] = 59
    hands["J9-S"] = 57
    hands["J8-S"] = 56
    hands["J7-S"] = 54
    hands["J6-S"] = 53
    hands["J5-S"] = 52
    hands["J4-S"] = 51
    hands["J3-S"] = 50
    hands["J2-S"] = 50
    hands["T9-S"] = 56
    hands["T8-S"] = 54
    hands["T7-S"] = 53
    hands["T6-S"] = 51
    hands["T5-S"] = 49
    hands["T4-S"] = 49
    hands["T3-S"] = 48
    hands["T2-S"] = 47
    hands["98-S"] = 53
    hands["97-S"] = 51
    hands["96-S"] = 50
    hands["95-S"] = 48
    hands["94-S"] = 46
    hands["93-S"] = 46
    hands["92-S"] = 45
    hands["87-S"] = 50
    hands["86-S"] = 49
    hands["85-S"] = 47
    hands["84-S"] = 45
    hands["83-S"] = 43
    hands["82-S"] = 43
    hands["76-S"] = 48
    hands["75-S"] = 46
    hands["74-S"] = 45
    hands["73-S"] = 43
    hands["72-S"] = 41
    hands["65-S"] = 46
    hands["64-S"] = 44
    hands["63-S"] = 42
    hands["62-S"] = 40
    hands["54-S"] = 44
    hands["53-S"] = 43
    hands["52-S"] = 41
    hands["43-S"] = 42
    hands["42-S"] = 40
    hands["32-S"] = 39

    return hands

def abstract(k):
    hands = init_hands()
    points = []
    for hand in hands:
        points.append((0, hands[hand], hand))
    print(points)
    clusters = k_means(k, points)
    for i in range(k):
        print("cluster " + str(i) + ":")
        for p in clusters[i]:
            print('  ', p)
    return clusters


def getBuckets(n=9):
    return abstract(n)

def cardToBucketMapper(n = 9):
    buckets = getBuckets(n)
    handToBucketMapper = {}
    for i,bucket in enumerate(buckets):
        for hand in bucket:
            handToBucketMapper[hand[2]] = i
    return handToBucketMapper

