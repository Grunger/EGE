// На основе решения А. Богданова
const B = 4;
begin
  var data := Readlines('27-22b.txt').Select(s->s.ToIntegers).ToArray;
  var n := data[0].First;
  var pairs := data.Skip(1).Take(n); 
  var sum := pairs.Sum(x->x.Min);
  pairs.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod 10) // сгруппировать по остаткам от деления на B
               .Select(x->x.Min)    // из каждой группы выбрать минимальное
               .ToArray)
    .Where(x->x mod 10 = 4)
    .Print;      
end.


