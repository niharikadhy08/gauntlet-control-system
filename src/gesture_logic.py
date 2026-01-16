def fingers_up(hand, hand_label=None):

    if hasattr(hand, "landmark"):
        lm = hand.landmark
    elif isinstance(hand, list):
        lm = hand
    else:
        return [0, 0, 0, 0, 0]

    fingers = [0, 0, 0, 0, 0]

    if hand_label == "Right":
        fingers[0] = lm[4].x < lm[3].x
    else:
        fingers[0] = lm[4].x > lm[3].x

    fingers[1] = lm[8].y < lm[6].y
    fingers[2] = lm[12].y < lm[10].y
    fingers[3] = lm[16].y < lm[14].y
    fingers[4] = lm[20].y < lm[18].y

    return fingers
