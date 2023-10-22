use std::fs;

fn first_task(assignments: &[&str]) {
    let mut separated: Vec<Vec<&str>> = vec![];
    let mut pairs: Vec<[i32; 2]> = vec![];
    for i in assignments {
        separated.push(i.split(',').collect::<Vec<&str>>());
    }
    for i in separated {
        for j in i {
            let x = j.split('-').collect::<Vec<&str>>();
            pairs.push([x[0].parse::<i32>().unwrap(), x[1].parse::<i32>().unwrap()]);
        }
    }

    let mut i = 0;
    let mut sum = 0;
    while i < pairs.len() {
        let first = pairs[i];
        let second = pairs[i + 1];
        i += 2;

        if (first[0] <= second[0] && first[1] >= second[1])
            || (second[0] <= first[0] && second[1] >= first[1])
        {
            sum += 1
        }
    }
    println!("first task: {sum}");
}

fn second_task(assignments: &[&str]) {
    let mut separated: Vec<Vec<&str>> = vec![];
    let mut pairs: Vec<[i32; 2]> = vec![];
    for i in assignments {
        separated.push(i.split(',').collect::<Vec<&str>>());
    }
    for i in separated {
        for j in i {
            let x = j.split('-').collect::<Vec<&str>>();
            pairs.push([x[0].parse::<i32>().unwrap(), x[1].parse::<i32>().unwrap()]);
        }
    }

    let mut i = 0;
    let mut sum = 0;
    while i < pairs.len() {
        let first = pairs[i];
        let second = pairs[i + 1];
        i += 2;

        if (first[1] > second[1] && first[0] <= second[1])
            || (second[1] > first[1] && second[0] <= first[1])
            || (first[0] < second[0] && first[1] >= second[0])
            || (second[0] < first[0] && second[1] >= first[0])
            || (first[0] == second[0]
                || first[1] == second[0]
                || first[0] == second[1]
                || first[1] == second[1])
        {
            sum += 1;
        }
    }
    println!("second task: {sum}");
}

fn main() {
    let input = fs::read_to_string("../input.txt").unwrap();
    let assignments = input.split('\n').collect::<Vec<&str>>();
    first_task(&assignments);
    second_task(&assignments);
}
