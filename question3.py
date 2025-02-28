import data as Data

cities = Data.cities # set of cities
scenarios = Data.scenarios # set of scenarios
theta = Data.theta # unit cost of delivery to city n in the first stage
theta_s = Data.theta_prime # unit cost of transportion between city n and center in the second stage

h = Data.h # unit cost of unused inventory
g = Data.g # unit cost of shortage 
I = Data.I # inventory of the center at the beginning
Yn = Data.Yn # inventory of city n at the beginning
demand = Data.demand # demand of city n under scenario k
prob = 1.0/len(scenarios) # probability of scenario k

import gurobipy as gp
from gurobipy import GRB

# 创建模型
model = gp.Model("Inventory_Management")

# 添加变量
x = model.addVars(cities, vtype=GRB.CONTINUOUS, name="x")
Q = model.addVars(scenarios, vtype=GRB.CONTINUOUS, name="Q")

u = model.addVars(cities, scenarios, vtype=GRB.CONTINUOUS, name="u")
v = model.addVars(cities, scenarios, vtype=GRB.CONTINUOUS, name="v")
z = model.addVars(cities, scenarios, vtype=GRB.CONTINUOUS, name="z")
s = model.addVars(cities, scenarios, vtype=GRB.CONTINUOUS, name="s")

# 目标函数
model.setObjective(gp.quicksum(theta[n] * x[n] for n in cities) + gp.quicksum(prob * Q[k] for k in scenarios), GRB.MINIMIZE)

# 约束条件
model.addConstr(gp.quicksum(x[n] for n in cities) <= I)

for k in scenarios:
    model.addConstr(I + gp.quicksum(u[n, k] for n in cities) >= gp.quicksum(v[n, k] + x[n] for n in cities), f"total_inventory_{k}")
    for n in cities:
        model.addConstr(Yn[n] + x[n] + v[n, k] + s[n, k] == demand.get((n, k), 0) + z[n, k] + u[n, k], f"city_inventory_{n}_{k}")
        model.addConstr(u[n, k] >= 0, f"non_negativity_u{n}_{k}")
        model.addConstr(v[n, k] >= 0, f"non_negativity_v{n}_{k}")
        model.addConstr(z[n, k] >= 0, f"non_negativity_z{n}_{k}")
        model.addConstr(s[n, k] >= 0, f"non_negativity_s{n}_{k}")

for n in cities:
    model.addConstr(x[n] >= 0, f"non_negativity_x_{n}")

# 第二阶段成本
for k in scenarios:
    model.addConstr(Q[k] == gp.quicksum(theta_s[n] * (u[n, k] + v[n, k]) + h * z[n, k] + g * s[n, k] for n in cities), f"cost_scenario_{k}")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for n in cities:
        print(f"x[{n}] = {x[n].X:.2f}")
else:
    print("No optimal solution found.")

print(f"Optimal value:{model.ObjVal:.2f}")