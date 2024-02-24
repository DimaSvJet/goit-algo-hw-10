import pulp as plp

prob = plp.LpProblem("Profit factory", plp.LpMaximize)

lemonade = plp.LpVariable("water", 0, None, cat=plp.LpContinuous)
fruit_juice = plp.LpVariable("sugar", 0, None, cat=plp.LpContinuous)

prob += lemonade + fruit_juice, "profit"

prob += 2 * lemonade + 1 * fruit_juice <=100, "water"
prob += 1 * lemonade + 0 * fruit_juice <=50, "sugar"
prob += 1 * lemonade + 0 * fruit_juice <=30, "lime juce"
prob += 0 * lemonade + 2 * fruit_juice <=40, "fruit puree"

prob.solve()

print("Status: ", {plp.LpStatus[prob.status]})
print(f'lemonade: {plp.value(lemonade)}')
print(f'fruit juice: {plp.value(fruit_juice)}')