def calculate_risk_score(hesitation_ratio, pauses_per_sentence, speech_rate):
    score = (
        hesitation_ratio * 0.5 +
        pauses_per_sentence * 0.3 -
        speech_rate * 0.2
    )
    return round(score, 2)
