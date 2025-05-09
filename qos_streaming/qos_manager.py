def qos_adjustment(decision_score):
    if decision_score > 0.8:
        return "Maintain Quality"
    elif decision_score > 0.5:
        return "Reduce Bitrate Slightly"
    else:
        return "Lower Resolution or Rebuffer"