use std::fs;

fn first_task(strategy: &[(&str, &str)]){
    let mut total_score = 0;
    let mut score = 0;
    for s in strategy.iter() {
        match s.1 {
            "X" => {
                score += 1;
                match s.0 {
                    "A" => score += 3,
                    "B" => {}
                    "C" => score += 6,
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Y" => {
                score += 2;
                match s.0 {
                    "A" => score += 6,
                    "B" => score += 3,
                    "C" => {}
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Z" => {
                score += 3;
                match s.0 {
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
    println!("first task: {total_score}");
}

fn second_task(strategy: &[(&str, &str)]) {
    let mut total_score = 0;
    let mut score = 0;
    for s in strategy.iter() {
        match s.1 {
            "X" => {
                match s.0 {
                    "A" => score += 3,
                    "B" => score += 1,
                    "C" => score += 2,
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Y" => {
                score += 3;
                match s.0 {
                    "A" => score += 1,
                    "B" => score += 2,
                    "C" => score += 3,
                    &_ => todo!("Cannot reach here"),
                }
            }
            "Z" => {
                score += 6;
                match s.0 {
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
    println!("second task: {total_score}");
}

fn main() {
    // Solution to first part two
    let input =
        fs::read_to_string("../input.txt").unwrap();
    let strategy = input
        .split('\n')
        .collect::<Vec<&str>>()
        .iter()
        .map(|x| {
            let mut a = x.split(' ');
            (a.next().unwrap(), a.next().unwrap())
        })
        .collect::<Vec<(&str, &str)>>();


    first_task(&strategy);
    second_task(&strategy);

}
