from OCC.Core.gp import gp_Pnt
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace
from OCC.Core.TColgp import TColgp_Array2OfPnt
from OCC.Core.GeomAPI import GeomAPI_PointsToBSplineSurface
from OCC.Core.GeomAbs import GeomAbs_C2
from OCC.Core.ShapeAnalysis import ShapeAnalysis_Surface, shapeanalysis_GetFaceUVBounds


p1 = gp_Pnt(-15, 200, 10)
p2 = gp_Pnt(5, 204, 0)
p3 = gp_Pnt(15, 200, 0)
p4 = gp_Pnt(-15, 20, 15)
p5 = gp_Pnt(-5, 20, 0)
p6 = gp_Pnt(15, 20, 35)

array = TColgp_Array2OfPnt(1, 3, 1, 2)
array.SetValue(1, 1, p1)
array.SetValue(2, 1, p2)
array.SetValue(3, 1, p3)
array.SetValue(1, 2, p4)
array.SetValue(2, 2, p5)
array.SetValue(3, 2, p6)
bspl_surf = GeomAPI_PointsToBSplineSurface(array, 3, 8, GeomAbs_C2,0.001).Surface()
face = BRepBuilderAPI_MakeFace(bspl_surf, 1e-6).Face()
umin, umax, vmin, vmax = shapeanalysis_GetFaceUVBounds(face)
print(umin, umax, vmin, vmax)

