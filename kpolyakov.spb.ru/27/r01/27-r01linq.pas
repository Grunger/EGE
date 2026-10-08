// На основе решения А. Богданова
uses sf;
const B = 6;
begin
  var data := Readlines('27-r01.txt').Sel(s->s.ToIs).ToA;
  var n := data[0].First;
  var pairs := data.Skip(1).Take(n); 
  var sum := pairs.Sum(x->x.Max);
  pairs.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на 6
               .Select(x->x.Max)    // из каждой группы выбрать максимальное
               .ToA)
    .Where(x->x.Divs(B))
    .Print;      
end.


