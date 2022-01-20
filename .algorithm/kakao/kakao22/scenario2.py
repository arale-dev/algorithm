import api
import collections

# 시나리오 2(problem = 2)


# global skill score
user_skill_score = {i: 40000 for i in range(1, 901)}
related = {i: set() for i in range(1, 901)}
already_matched = []


def main():
    # start round
    start = api.post_start(2)
    turn = start.get("time")

    pairs = []
    for turn in range(1, 596):
        # print(user_skill_score)
        match = api.put_match(pairs)
        # print(">>>", match)

        # 매칭
        # pairs = first_two_match()
        pairs = min_diff(turn)
        # pairs = match_diff_with_wait(turn) # 0일 때 {'status': 'finished', 'efficiency_score': '99.9254', 'accuracy_score1': '34.4444', 'accuracy_score2': '47.6758', 'score': '178.4846'}

        # 점수 업데이트
        # winner_always_win()
        # update_with_ratio()
        # update_related()
        update_all_related()

    set_user_rank()
    match = api.put_match([])
    # print(">>>???", match)
    score = api.get_score()


# 매칭 방법 2
# {'status': 'finished', 'efficiency_score': '99.8733', 'accuracy_score1': '36.6667', 'accuracy_score2': '49.4751', 'score': '183.2687'}
def min_diff(turn):
    global user_skill_score
    pairs = []
    waiting_line = api.get_waiting_line()

    if (len(waiting_line) >= 2):
        matched = []
        waiting_ids = [user["id"] for user in waiting_line]
        waiting_times = {user["id"]: user["from"] for user in waiting_line}
        i_j_diff = [[i, j, abs(user_skill_score[i] - user_skill_score[j])] for i in waiting_ids for j in waiting_ids if
                    i < j]

        sorted_i_j_diff = sorted(i_j_diff, key=lambda item: item[2])
        for i, j, diff in sorted_i_j_diff:
            if i not in matched and j not in matched:
                pairs.append([i, j])
                matched.extend([i, j])

    return pairs


# 점수 업데이트 방법 4
def update_all_related():
    global user_skill_score
    global related
    game_results = api.get_game_result()
    for game in game_results:
        win, lose, taken = game["win"], game["lose"], game["taken"]

        skill_difference = (40 - taken)  # - 5)
        skill_difference = skill_difference * 99000 / 35

        origin_win = user_skill_score[win]
        origin_lose = user_skill_score[lose]

        origin_center = user_skill_score[win] + user_skill_score[lose] / 2
        expected_win = origin_center + skill_difference / 2
        expected_lose = origin_center - skill_difference / 2
        expected_win_ratio = expected_win / (expected_win + expected_lose)
        expected_lose_ratio = expected_lose / (expected_win + expected_lose)
        new_win = expected_win * expected_win_ratio + expected_lose * expected_lose_ratio
        new_lose = expected_win * expected_lose_ratio + expected_lose * expected_win_ratio
        user_skill_score[win] = new_win
        user_skill_score[lose] = new_lose

        # 연관된거 일관적으로 다 더해버리기 {'status': 'finished', 'efficiency_score': '99.8728', 'accuracy_score1': '38.8889', 'accuracy_score2': '50.0587', 'score': '186.6353'}
        checked_related = []
        remain_related = collections.deque(related[win])
        while remain_related:
            user_updating = remain_related.popleft()
            if user_updating in checked_related:
                continue
            user_skill_score[user_updating] += new_win - origin_win
            remain_related.extend(related[user_updating])
            checked_related.append(user_updating)
        checked_related = []
        remain_related = collections.deque(related[lose])
        while remain_related:
            user_updating = remain_related.popleft()
            if user_updating in checked_related:
                continue
            user_skill_score[user_updating] += new_lose - origin_lose
            remain_related.extend(related[user_updating])
            checked_related.append(user_updating)

        related[win].add(lose)
        related[lose].add(win)


# 점수 바탕으로 랭크 정하기
def set_user_rank():
    global user_skill_score
    sorted_user_with_skill = sorted(user_skill_score.items(), reverse=True, key=lambda item: int(item[1]))

    set_data = []
    rank = 1
    latest_score = 0
    for i in range(1, len(sorted_user_with_skill) + 1):  # 공동 순위 고려 : {'status': 'finished', 'efficiency_score': '99.8728', 'accuracy_score1': '46.4444', 'accuracy_score2': '50.0587', 'score': '195.702'}
        user_id, score = sorted_user_with_skill[i - 1]
        if latest_score != score:
            latest_score = score
            rank = i
        set_data.append({"id": user_id, "grade": rank})
    api.put_change_grade(set_data)


if __name__ == "__main__":
    main()
