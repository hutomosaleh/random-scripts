import numpy as np

from sympy.solvers import solve
from sympy import Symbol

"""
	Gleichung aus der Volesung Berechnung elektrischer Maschine
"""

def bem_solver(I_N=None, P_N=None, U_Nstr=None, theta_N=None, eta_N=None, fall="stern"):
    var = {"I_N": I_N, "P_N": P_N, "U_Nstr": U_Nstr, "theta_N": theta_N, "eta_N": eta_N}
    limit = 0
    for key, value in var.items():
        if var[key] is None:
            limit += 1
            our_x = var[key] = Symbol("X")

        if limit == 2:
            raise ValueError("Needs more arguments!")
    if limit == 0:
        raise ValueError("Too many arguments!")

    if fall == "stern":
        var["U_Nstr"] = var["U_Nstr"] / np.sqrt(3)
    else:
        var["U_Nstr"] = var["U_Nstr"]

    equation = var["I_N"] - var["P_N"] / (3 * var["U_Nstr"] * np.cos(var["theta_N"]) * var["eta_N"])
    res = result(equation, our_x)

    return res


def result(equation, x):
    return solve(equation, x)


print(bem_solver(I_N=391.351509646086, P_N=None, U_Nstr=690, theta_N=np.deg2rad(25.81), eta_N=0.95))



