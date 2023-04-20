const limit_problems = [
  ["lim (x->5) x^2", 25],
  ["lim (x->1) (x+3)/(x+1)", 2],
  ["lim (x->inf) 1/x", 0],
  ["lim (x->-inf) 1/x", 0],
  ["lim (x->1) 2/(x+1)", 1],
  ["lim (x->1) (2x-2)/(x-1)", 2],
  ["lim (x->0) (x^2566)/(x^2566)", 1],
  ["lim (x->0) (x^2023)/(x^2023)", 1],
  ["lim (x->inf) (x^2566)/(x^2566)", 1],
  ["lim (x->inf) (x^2023)/(x^2023)", 1],
  ["lim (x->-1) (x+1)/(x-1)", 0],
  ["lim (x->0) (x-1)/(x^2)", -Infinity],
  ["lim (x->2) 10/(x+3)", 2],
  ["lim (x->2) (x^2-4)/(x-2)", 4],
  ["lim (x->-2) (x^2-4)/(x+2)", -4],
  ["lim (x->0) 2^x", 1],
  ["lim (x->0) 1/(x^2)", Infinity],
  ["lim (x->inf) (x^2566)/(x^2023)", Infinity],
  ["lim (x->inf) (x^2023)/(x^2566)", 0],
  ["lim (x->0) (x^2566)/(x^2023)", 0],
  ["lim (x->0) 1/(x^2566)", Infinity],
  ["lim (x->0) 123456789*x", Infinity],
];

const limit_problems_trig_log_expo = [
    ["lim (x->0) e^x", 1],
    ["lim (x->0) sin(x)", 0],
    ["lim (x->0) sin(x)*1234567890", 0],
];

const limit_problems_log_lhospital = [
];

const limit_problems_log_lhospital_trig_log_expo = [
];

const limit_problems_log_diverge = [
];

const limit_problems_log_diverge_trig_log_expo = [
];