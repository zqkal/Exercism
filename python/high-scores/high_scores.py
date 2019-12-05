def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    scores.sort()
    result = scores[::-1]
    return result[:3]