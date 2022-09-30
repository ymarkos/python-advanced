from collections import deque

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120


effects = deque(int(x) for x in input().split(', '))
casings = [int(x) for x in input().split(', ')]


min_datura = 3
min_cherry = 3
min_smoke_decoy = 3

actual_count_datura = 0
actual_count_cherry = 0
actual_count_decoy = 0
is_full = False

while True:
    if len(effects) == 0 or len(casings) == 0 or is_full:
        break
    cur_effect = effects.popleft()
    cur_casing = casings.pop()
    cur_sum = cur_casing + cur_effect
    if cur_sum == DATURA_BOMBS:
        min_datura -= 1
        actual_count_datura +=1

    elif cur_sum == CHERRY_BOMBS:
        min_cherry -=1
        actual_count_cherry +=1

    elif cur_sum == SMOKE_DECOY_BOMBS:
        min_smoke_decoy -= 1
        actual_count_decoy +=1
    else:
        effects.appendleft(cur_effect)
        casings.append(cur_casing-5)
    if min_cherry <= 0 and min_datura <= 0 and min_smoke_decoy <= 0:
        is_full = True

if is_full:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print(f"Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print(f"Bomb Casings: empty")

print(f"Cherry Bombs: {actual_count_cherry}")
print(f"Datura Bombs: {actual_count_datura}")
print(f"Smoke Decoy Bombs: {actual_count_decoy}")
