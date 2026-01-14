import twophase.solver  as sv
import twophase.cubie as cubie

cubestring = 'RFBBULRDFLBRFRRDLUFFUUFRLURDLFFDDDUBUDUDLRFLBDUBBBRLBL'
solution = sv.solve(cubestring, 20, 1)
solution = solution.split(' ')

print(cubie.basicMoveCube[0])

