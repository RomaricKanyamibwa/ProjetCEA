*  Homology and cohomology computation
*
*********************************************************************/
// Homology computation in Gmsh finds representative chains of (relative)
// (co)homology space bases using a mesh of a model.  The representative basis
// chains are stored in the mesh as physical groups of Gmsh, one for each chain.
// Create an example geometry
m = 0.5; // mesh characteristic length
h = 5; // height in the z-direction
Point(1) = {0, 0, 0, m};   Point(2) = {10, 0, 0, m};
Point(3) = {10, 10, 0, m}; Point(4) = {0, 10, 0, m};
Point(5) = {4, 4, 0, m};   Point(6) = {6, 4, 0, m};
Point(7) = {6, 6, 0, m};   Point(8) = {4, 6, 0, m};
Point(9) = {2, 0, 0, m};   Point(10) = {8, 0, 0, m};
Point(11) = {2, 10, 0, m}; Point(12) = {8, 10, 0, m};
Line(1) = {1, 9};  Line(2) = {9, 10}; Line(3) = {10, 2};
Line(4) = {2, 3};  Line(5) = {3, 12}; Line(6) = {12, 11};
Line(7) = {11, 4}; Line(8) = {4, 1};  Line(9) = {5, 6};
Line(10) = {6, 7}; Line(11) = {7, 8}; Line(12) = {8, 5};
Line Loop(13) = {6, 7, 8, 1, 2, 3, 4, 5};
Line Loop(14) = {11, 12, 9, 10};
Plane Surface(15) = {13, 14};
Extrude {0, 0, h}{ Surface{15}; }
Physical Volume(1) = {1};
Line Loop(100) = {20,21,22,23,24,17,18,19};
Line Loop(101) = {25,28,27,26};
Plane Surface(102) = {100, 101};
Line Loop(102) = {1,2,3,51,22,21,20,39};
Line Loop(103) = {4,55,23,51};
Line Loop(104) = {5,6,7,35,18,17,24,55};
Line Loop(105) = {8,35,19,39};
Line Loop(106) = {9,63,26,67};
Line Loop(107) = {10,63,25,62};
Line Loop(108) = {11,70,28,62};
Line Loop(109) = {12,71,27,67};
Physical Surface(110) = {102};
Physical Surface(111) = {103};
Physical Surface(112) = {104};
Physical Surface(113) = {105};
Physical Surface(114) = {106};
Physical Surface(115) = {107};
Physical Surface(116) = {108};
Physical Surface(117) = {109};
Homology {{1}, {15, 102, 110, 111,112,113,114,115,116,117}};
