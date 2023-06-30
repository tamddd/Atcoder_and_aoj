let x, y, z = Scanf.sscanf (read_line ()) "%d %d %d" (fun x y z ->
                  if y < 0 then
                    (-x, -y, -z)
                else (x, y, z))
let ans =
  if x < y then abs x
else if z > y then -1
else (abs z) + abs (x - z)

let () = print_int ans
