// Автор: А. Богданов
##
var p := readLines('27-70a.txt').Skip(1)
   .Select(s->s.ToIntegers).ToArray;
var g := p.Sum(r->r.Sum).Println;
var s := p.Aggregate(|0|,(a,r)->
  a.Cartesian(r,(x,y)->x+y)
   .GroupBy(z->z mod 5)
   .Select(g->g.Max)
   .ToArray);
//s.Order.Println;
//s.Select(x->g-x).Order.Println;
s.Select(x->x-(g-x)).Where(x->x.Divs(5)).Max.Print;   