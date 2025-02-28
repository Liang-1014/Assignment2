import gurobipy as gp
from gurobipy import GRB

# Stochastic program
# 创建模型
model = gp.Model("ScotRail_Optimization_stochastic")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, 4, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    0.4 * (3 * y[0, 0] + 2 * y[1, 0] + y[2, 0]) +
    0.3 * (3 * y[0, 1] + 2 * y[1, 1] + y[2, 1]) +
    0.2 * (3 * y[0, 2] + 2 * y[1, 2] + y[2, 2]) +
    0.1 * (3 * y[0, 3] + 2 * y[1, 3] + y[2, 3]),
    GRB.MAXIMIZE
)

# 添加约束条件
for i in range(3):
    for j in range(4):
        model.addConstr(y[i, j] <= x[i], f"c_{i}_{j}")

model.addConstrs((y[0, j] <= [25, 20, 10, 5][j] for j in range(4)), "y1")
model.addConstrs((y[1, j] <= [60, 40, 25, 10][j] for j in range(4)), "y2")
model.addConstrs((y[2, j] <= [200, 180, 175, 150][j] for j in range(4)), "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for i in range(3):
        print(f"x[{i+1}] = {x[i].X}")
        for j in range(4):
            print(f"y[{i+1},{j+1}] = {y[i, j].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")

stochastic_solution = model.ObjVal


# Mean-value problem
mean_firstclass = 18.5
mean_businessclass = 42
mean_economyclass = 184
obj = []
# 创建模型
model = gp.Model("ScotRail_Optimization_mean")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)

# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= mean_firstclass, "y1")
model.addConstr(y[1] <= mean_businessclass, "y2")
model.addConstr(y[2] <= mean_economyclass, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for i in range(3):
        print(f"x[{i+1}] = {x[i].X}")
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")

x_mean = [x[0].X,x[1].X,x[2].X]

# 创建模型
model = gp.Model("ScotRail_Optimization_mean_1")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)

model.addConstr(x[0] == x_mean[0], "x1")
model.addConstr(x[1] == x_mean[1], "x2")
model.addConstr(x[2] == x_mean[2], "x3")

# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 25, "y1")
model.addConstr(y[1] <= 60, "y2")
model.addConstr(y[2] <= 200, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("1.Optimal solution found:")
    for i in range(3):
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")

obj.append(model.ObjVal)

model = gp.Model("ScotRail_Optimization_mean_2")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)

model.addConstr(x[0] == x_mean[0], "x1")
model.addConstr(x[1] == x_mean[1], "x2")
model.addConstr(x[2] == x_mean[2], "x3")

# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 20, "y1")
model.addConstr(y[1] <= 40, "y2")
model.addConstr(y[2] <= 180, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("2.Optimal solution found:")
    for i in range(3):
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")

obj.append(model.ObjVal)

model = gp.Model("ScotRail_Optimization_mean_3")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)

model.addConstr(x[0] == x_mean[0], "x1")
model.addConstr(x[1] == x_mean[1], "x2")
model.addConstr(x[2] == x_mean[2], "x3")

# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 10, "y1")
model.addConstr(y[1] <= 25, "y2")
model.addConstr(y[2] <= 175, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("3.Optimal solution found:")
    for i in range(3):
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")

obj.append(model.ObjVal)

model = gp.Model("ScotRail_Optimization_mean_4")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)

model.addConstr(x[0] == x_mean[0], "x1")
model.addConstr(x[1] == x_mean[1], "x2")
model.addConstr(x[2] == x_mean[2], "x3")

# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 5, "y1")
model.addConstr(y[1] <= 10, "y2")
model.addConstr(y[2] <= 150, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("2.Optimal solution found:")
    for i in range(3):
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")

obj.append(model.ObjVal)

# Perfect information
obj_p = []
model = gp.Model("ScotRail_Optimization_perfect_1")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)
# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 25, "y1")
model.addConstr(y[1] <= 60, "y2")
model.addConstr(y[2] <= 200, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("2.Optimal solution found:")
    for i in range(3):
        print(f"x[{i+1}] = {x[i].X}")
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")
obj_p.append(model.ObjVal)

model = gp.Model("ScotRail_Optimization_perfect_2")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)
# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 20, "y1")
model.addConstr(y[1] <= 40, "y2")
model.addConstr(y[2] <= 180, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("2.Optimal solution found:")
    for i in range(3):
        print(f"x[{i+1}] = {x[i].X}")
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")
obj_p.append(model.ObjVal)

model = gp.Model("ScotRail_Optimization_perfect_3")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)
# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 10, "y1")
model.addConstr(y[1] <= 25, "y2")
model.addConstr(y[2] <= 175, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("2.Optimal solution found:")
    for i in range(3):
        print(f"x[{i+1}] = {x[i].X}")
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")
obj_p.append(model.ObjVal)

model = gp.Model("ScotRail_Optimization_perfect_4")

# 添加变量
x = model.addVars(3, vtype=GRB.INTEGER, name="x")
y = model.addVars(3, vtype=GRB.INTEGER, name="y")

# 设置目标函数
model.setObjective(
    3 * y[0] + 2 * y[1] + y[2],
    GRB.MAXIMIZE
)
# 添加约束条件
for i in range(3):
        model.addConstr(y[i] <= x[i], f"c_{i}")

model.addConstr(y[0] <= 5, "y1")
model.addConstr(y[1] <= 10, "y2")
model.addConstr(y[2] <= 150, "y3")

model.addConstr(2 * x[0] + 1.5 * x[1] + x[2] <= 200, "total_capacity")

# 求解模型
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("2.Optimal solution found:")
    for i in range(3):
        print(f"x[{i+1}] = {x[i].X}")
        print(f"y[{i+1}] = {y[i].X}")
    print(f"Objective value = {model.objVal}")
else:
    print("No optimal solution found.")
obj_p.append(model.ObjVal)

print(obj)
print(obj_p)
mean_value_solution = 0.4*obj[0]+0.3*obj[1]+0.2*obj[2]+0.1*obj[3]
perfect_solution = 0.4*obj_p[0]+0.3*obj_p[1]+0.2*obj_p[2]+0.1*obj_p[3]
VSS = stochastic_solution - mean_value_solution
EVPI = perfect_solution - stochastic_solution
print ( f" Stochastic Solution = {stochastic_solution}"
)
print ( f" Mean Value Solution = {mean_value_solution}"
)
print ( f" Perfect Solution = {perfect_solution}"
)
print ( f"VSS = {VSS}"
)
print ( f"EVPI = {EVPI}"
)