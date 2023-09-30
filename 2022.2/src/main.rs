use std::fs;

fn main() {
    // Solution to first part two
    let contents =
        fs::read_to_string("./input.txt").unwrap();
    let vec = contents
        .split('\n')
        .collect::<Vec<&str>>()
        .iter()
        .map(|x| {
            let mut a = x.split(' ');
            (a.next().unwrap(), a.next().unwrap())
        })
        .collect::<Vec<(&str, &str)>>();

    let mut total_score = 0;
    let mut score = 0;
    for v in vec.iter() {
        match v.1 {
            "X" => {
                match v.0 {
                    "A" => score += 3,
                    "B" => score += 1,
                    "C" => score += 2,
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Y" => {
                score += 3;
                match v.0 {
                    "A" => score += 1,
                    "B" => score += 2,
                    "C" => score += 3,
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Z" => {
                score += 6;
                match v.0 {
                    "A" => score += 2,
                    "B" => score += 3,
                    "C" => score += 1,
                    &_ => todo!("Cannot reach here"),
                }
            }
            &_ => todo!("Cannot reach here"),
        }
        total_score += score;
        score = 0;
    }
    println!("{total_score}");
}