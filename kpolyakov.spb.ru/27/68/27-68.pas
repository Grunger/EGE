// Автор: А. Богданов
##
Readlines('27-68a.txt').Skip(1)
  .Select( s->s.ToIntegers ) 
  .Select( v->v.Combinations(2)
               .Select(s->s.Sum).ToArray )
  .Aggregate( |0|,(a,r) -> 
     a.Cartesian(r, (x,y) -> x+y )
      .GroupBy( s -> s mod 51 )
      .Select( g -> g.Min )
      .ToArray)
  .Where( s -> s.Divs(3) xor s.Divs(17) )
  .Min.Println;
