// На основе решения А. Богданова
const B = 2;
begin
  var data := Readlines('27-40b.txt').Select(s->s.ToIntegers).ToArray;
  var n := data[0].First;
  var pairs := data.Skip(1).Take(n); 
  var sum := pairs.Sum(x->x.Sum);
  pairs.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на B
               .Select(x->x.Max)    // из каждой группы выбрать максимальное
               .ToArray)
    .Where(x->(sum-x).IsOdd)
    .Max
    .Print;      
end.


