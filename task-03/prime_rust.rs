use std::io;
fn is_prime(n: i32) -> bool {
    if n <= 1 {
        return false;
    }
    for i in 2..n {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn print_prime(n: i32) {
    for i in 2..=n {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
}

fn main() {
   println!("Please enter an integer:");
  let mut input = String::new();

  io::stdin()
      .read_line(&mut input)
      .expect("Failed to read line");

    
  let n: i32 = input.trim().parse().expect("Please enter a valid integer");

  print_prime(n);
}
