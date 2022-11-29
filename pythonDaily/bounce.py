
ht = 30
b = .75
w = 1.5

def bouncing_ball(h, bounce, window):
    passes = 0
    while h > window:
        passes += 1
        if h * bounce > window: passes += 1
        h -= h - (h * bounce)
        print(h)
    return passes or -1

print(bouncing_ball(ht, b, w))