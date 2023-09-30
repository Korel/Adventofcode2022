use std::fs;

fn main() {
    let input = fs::read_to_string("./input.txt").unwrap();
    let input_parsed = input.split('\n').collect::<Vec<&str>>();
    let mut parsed2: Vec<Vec<&str>> = vec![];
    let mut parsed3: Vec<[i32; 2]> = vec![];
    for i in input_parsed {
        parsed2.push(i.split(',').collect::<Vec<&str>>());
    }
    for i in parsed2 {
        for j in i {
            let x = j.split('-').collect::<Vec<&str>>();
            parsed3.push([x[0].parse::<i32>().unwrap(), x[1].parse::<i32>().unwrap()]);
        }
    }

    let mut i = 0;
    let mut sum = 0;
    while i < parsed3.len() {
        let first = parsed3[i];
        let second = parsed3[i + 1];
        i += 2;

        if (first[0] <= second[0] && first[1] >= second[1])
            || (second[0] <= first[0] && second[1] >= first[1])
        {
            sum += 1
        }
    }
    println!("{}", sum);

}
