use std::fs;

fn main() {
    let contents =
        fs::read_to_string("../input.txt").unwrap();
    let vec: Vec<&str> = contents.split("\n").collect();
    let mut calories: Vec<u64> = vec![];
    let mut calorie: u64 = 0;
    for str in vec {
        let parsed = str.parse::<u64>();
        match parsed {
            Ok(n) => calorie += n,
            Err(_) => {
                calories.push(calorie);
                calorie = 0;
            }
        }
    }

    let mut max0: u64 = 0;
    let mut max1: u64 = 0;
    let mut max2: u64 = 0;

    for c in calories.iter() {
        if *c > max2 {
            max0 = max1;
            max1 = max2;
            max2 = *c;
        } else if *c > max1 {
            max0 = max1;
            max1 = *c;
        } else if *c > max0 {
            max0 = *c;
        }
    }

    println!("First task: {max2}");
    println!("Second task: {}", max0 + max1 + max2);
}
