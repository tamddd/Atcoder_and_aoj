let n, d = Scanf.sscanf (read_line ()) "%d %d" (fun a b -> (a, b))

let ans =
  let ln = d * 2 + 1 in
  (n + ln - 1) / ln

let () = print_int (ans)
