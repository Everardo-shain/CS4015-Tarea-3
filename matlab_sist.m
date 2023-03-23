syms x y z
eqn1 = x + 3*y  == 300;
eqn2 = 1.5*x + 2*y == 350;
sol = solve([eqn1, eqn2], [x, y, z]);
xSol = sol.x
ySol = sol.y