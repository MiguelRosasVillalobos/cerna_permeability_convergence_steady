SetFactory("OpenCASCADE");
v() = ShapeFromFile("./geometry_script/geometry.step");
BooleanFragments{ Volume{v()}; Delete; }{}
//+
lc = $lccc;
rd = $rdd;
l1 = $l11;
a = $aa;
//+
Mesh.MeshSizeMax = lc;
