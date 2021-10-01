#include "costmap_2d.h"
using namespace costmap_2d;

int main()
{
    Costmap2D obj;
    obj.initMaps(10,10);
    obj.setCost(1,1,100);
    obj.saveMap("save.pgm");
} 