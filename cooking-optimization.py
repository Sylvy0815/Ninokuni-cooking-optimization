# 재료 사용량을 고려한 새로운 요리 제작 횟수 계산
# 이번에는 각 요리의 현재 개수를 고려하여 재료의 균형을 맞춤

# 재료 및 요리 정보 재정의
ingredients = {
    "곡물": 345,
    "야채": 2342,
    "고기": 442,
    "생선": 325,
    "우유": 752,
    "계란": 722,
    "버섯": 659,
    "향신료": 394
}

# 현재 요리 개수
current_dishes = {
    "타르타르 소스와 튀김": 147,
    "최고의 칠리 새우": 129,
    "극상의 숯불 불고기": 149,
    "땅콩 경단": 124,
    "살구 설탕절임": 130,
    "바닷바람 카르파초": 116,
    "비싼 성게소스 뫼니에르": 176
}

recipes = {
    "타르타르 소스와 튀김": {"생선": 1, "야채": 3, "계란": 1},
    "최고의 칠리 새우": {"생선": 1, "버섯": 1, "고기": 3, "우유": 1},
    "극상의 숯불 불고기": {"향신료": 1, "고기": 3, "버섯": 1},
    "땅콩 경단": {"계란": 1, "버섯": 1, "곡물": 3, "우유": 1},
    "살구 설탕절임": {"향신료": 1, "야채": 3, "우유": 1},
    "바닷바람 카르파초": {"생선": 2, "향신료": 1, "야채": 3, "계란": 1},
    "비싼 성게소스 뫼니에르": {"생선": 2, "버섯": 1, "곡물": 3, "우유": 1}
}

# 요리의 최대 횟수를 계산하는 함수 정의
def calculate_max_dishes(ingredients, recipes, current_dishes):
    dishes_count = {dish: 0 for dish in recipes.keys()}
    remaining_ingredients = ingredients.copy()

    # 모든 재료가 소진될 때까지 반복
    while True:
        made_dish = False

        for dish, recipe in recipes.items():
            # 이 요리를 만들 수 있는지 확인
            if all(remaining_ingredients[ing] >= amt for ing, amt in recipe.items()):
                # 요리 제작
                for ing, amt in recipe.items():
                    remaining_ingredients[ing] -= amt
                dishes_count[dish] += 1
                made_dish = True

        # 더 이상 요리를 만들 수 없으면 중단
        if not made_dish:
            break

    # 최종 요리 개수 (현재 개수 포함)
    final_dishes_count = {dish: current_dishes[dish] + dishes_count[dish] for dish in dishes_count}

    return final_dishes_count, remaining_ingredients

# 최대 요리 횟수 계산
final_dishes_count, remaining_ingredients = calculate_max_dishes(ingredients, recipes, current_dishes)

print(final_dishes_count)
print(remaining_ingredients)
