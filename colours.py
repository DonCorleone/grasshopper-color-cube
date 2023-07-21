import rhinoscriptsyntax as rs
import System.Drawing as sd

step = int(step)
min = int(min)
max = int(max)

points = []
colours = []

for x in range(min, max, step):
    for y in range(min, max, step):
        for z in range(min, max, step):
            points.append(rs.AddPoint(x, y, z))
            colours.append(sd.Color.FromArgb(x, y, z))