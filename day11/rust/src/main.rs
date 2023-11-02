use num::integer::lcm;
use std::fs;

#[derive(Debug, Clone)]
struct Monkey {
    items: Vec<i64>,
    operation: (String, i64),
    test: i64,
    throw: (usize, usize),
    inspection: i64,
}

fn parse_input(lines: Vec<&str>) -> Vec<Monkey> {
    let mut monkeys = Vec::new();
    for line in lines {
        if line.is_empty() {
            continue;
        }
        let mut chars = line.chars();
        let char0 = chars.next().unwrap();
        if char0 == 'M' {
            monkeys.push(Monkey {
                items: Vec::new(),
                operation: ("".to_string(), 0),
                test: 0,
                throw: (0, 0),
                inspection: 0,
            });
            continue;
        }

        let char3 = chars.nth(1).unwrap();
        if char3 == 'S' {
            let monkey = monkeys.last_mut().unwrap();
            let items: Vec<i64> = line[line.find(':').unwrap() + 1..]
                .split(',')
                .map(|x| x[1..].parse::<i64>().unwrap())
                .collect();
            monkey.items = items;
        }
        if char3 == 'O' {
            let monkey = monkeys.last_mut().unwrap();
            let after_equal = line[line.find('=').unwrap() + 1..].to_string();
            let split_add = after_equal.split('+').collect::<Vec<&str>>();
            let split_mul = after_equal.split('*').collect::<Vec<&str>>();
            if split_add.len() == 2 {
                monkey.operation.0 = "add".to_string();
                monkey.operation.1 = if split_add[1].contains("old") {
                    -1
                } else {
                    split_add[1][1..].parse::<i64>().unwrap()
                };
            } else {
                monkey.operation.0 = "mul".to_string();
                monkey.operation.1 = if split_mul[1].contains("old") {
                    -1
                } else {
                    split_mul[1][1..].parse::<i64>().unwrap()
                };
            }
            continue;
        }

        if char3 == 'T' {
            let monkey = monkeys.last_mut().unwrap();
            monkey.test = line[line.find("by ").unwrap() + "by ".len()..]
                .parse::<i64>()
                .unwrap();
            continue;
        }

        let char5 = chars.nth(1).unwrap();
        if char5 == 'I' {
            // It must be I anyway but still...
            let monkey = monkeys.last_mut().unwrap();
            let value = line[line.find("monkey ").unwrap() + "monkey ".len()..]
                .parse::<usize>()
                .unwrap();
            if line.contains("true") {
                monkey.throw.0 = value;
            } else {
                monkey.throw.1 = value;
            }
        }
    }

    monkeys
}

fn first_task(mut monkeys: Vec<Monkey>) -> i64 {
    for _ in 0..20 {
        for i in 0..monkeys.len() {
            while !monkeys[i].items.is_empty() {
                let item = monkeys[i].items[0];
                monkeys[i].items.remove(0);
                monkeys[i].inspection += 1;
                let operation_value = if monkeys[i].operation.1 == -1 {
                    item
                } else {
                    monkeys[i].operation.1
                };
                let worry = if monkeys[i].operation.0 == "add" {
                    (item + operation_value) / 3
                } else {
                    (item * operation_value) / 3
                };
                if worry % monkeys[i].test == 0 {
                    let index = monkeys[i].throw.0;
                    monkeys[index].items.push(worry);
                } else {
                    let index = monkeys[i].throw.1;
                    monkeys[index].items.push(worry);
                }
            }
        }
    }
    let mut inspections = monkeys.iter().map(|x| x.inspection).collect::<Vec<i64>>();
    inspections.sort();
    inspections[inspections.len() - 1] * inspections[inspections.len() - 2]
}

fn second_task(mut monkeys: Vec<Monkey>) -> i64 {
    let mut test_lcm: i64 = 1;
    for monkey in monkeys.iter() {
        test_lcm = lcm(test_lcm, monkey.test);
    }
    for _count in 0..10000 {
        for i in 0..monkeys.len() {
            while !monkeys[i].items.is_empty() {
                let item = monkeys[i].items[0];
                monkeys[i].items.remove(0);
                monkeys[i].inspection += 1;
                let operation_value = if monkeys[i].operation.1 == -1 {
                    item
                } else {
                    monkeys[i].operation.1
                };
                let worry = if monkeys[i].operation.0 == "add" {
                    item + operation_value
                } else {
                    item * operation_value
                };
                if worry % monkeys[i].test == 0 {
                    let index = monkeys[i].throw.0;
                    monkeys[index].items.push(worry);
                } else {
                    let index = monkeys[i].throw.1;
                    monkeys[index].items.push(worry % test_lcm);
                }
            }
        }
    }
    let mut inspections = monkeys.iter().map(|x| x.inspection).collect::<Vec<i64>>();
    inspections.sort();
    inspections[inspections.len() - 1] * inspections[inspections.len() - 2]
}

fn main() {
    let file_content = fs::read_to_string("../input.txt").unwrap();
    let monkeys = parse_input(file_content.lines().collect());
    let first_task_result = first_task(monkeys.clone());
    let second_task_result = second_task(monkeys);
    println!("first_task: {first_task_result}");
    println!("second_task: {second_task_result}");
    // Assertion values are obtained from output of python script.
    assert_eq!(first_task_result, 110220);
    assert_eq!(second_task_result, 19457438264);
}
