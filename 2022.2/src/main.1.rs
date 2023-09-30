use std::fs;

fn main() {
    // Solution to first part one
    let contents =
        fs::read_to_string("/home/korel/projects/adventofcode/2022.2/input.txt").unwrap();
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
                score += 1;
                match v.0 {
                    "A" => score += 3,
                    "B" => {}
                    "C" => score += 6,
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Y" => {
                score += 2;
                match v.0 {
                    "A" => score += 6,
                    "B" => score += 3,
                    "C" => {}
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Z" => {
                score += 3;
                match v.0 {
                    "A" => {}
                    "B" => score += 6,
                    "C" => score += 3,
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
