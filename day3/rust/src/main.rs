use std::collections::HashMap;
use std::fs;

fn first_task(contents: &[&str], map: &HashMap<char, u64>) {
    let mut sum: u64 = 0;
    for item in contents.into_iter() {
        let split = item.split_at(item.len() / 2);
        // Simple solution
        'outer: for c0 in split.0.chars().into_iter() {
            for c1 in split.1.chars().into_iter() {
                if c0 == c1 {
                    sum += map.get(&c0).unwrap();
                    break 'outer;
                }
            }
        }
    }
    println!("first task: {sum}");
}

fn second_task(contents: &[&str], map: &HashMap<char, u64>) {
    let mut sum: u64 = 0;
    let mut vec = vec![contents.split_at(3)];
    while !vec.last().unwrap().1.is_empty() {
        vec.push(vec.last().unwrap().1.split_at(3));
    }

    for split in vec.into_iter() {
        let str1 = split.0[0].clone();
        let str2 = split.0[1].clone();
        let str3 = split.0[2].clone();
        let mut matches = String::new();

        for c in str2.chars() {
            if str1.find(c).is_some() {
                matches.push(c);
            }
        }
        for c in str3.chars() {
            if matches.find(c).is_some() {
                sum += map.get(&c).unwrap();
                break;
            }
        }
    }
    println!("second task: {sum}");
}

fn main() {
    let input = fs::read_to_string("../input.txt").unwrap();
    let contents = input.split('\n').collect::<Vec<&str>>();

    let map = HashMap::from([
        ('a', 1),
        ('b', 2),
        ('c', 3),
        ('d', 4),
        ('e', 5),
        ('f', 6),
        ('g', 7),
        ('h', 8),
        ('i', 9),
        ('j', 10),
        ('k', 11),
        ('l', 12),
        ('m', 13),
        ('n', 14),
        ('o', 15),
        ('p', 16),
        ('q', 17),
        ('r', 18),
        ('s', 19),
        ('t', 20),
        ('u', 21),
        ('v', 22),
        ('w', 23),
        ('x', 24),
        ('y', 25),
        ('z', 26),
        ('A', 27),
        ('B', 28),
        ('C', 29),
        ('D', 30),
        ('E', 31),
        ('F', 32),
        ('G', 33),
        ('H', 34),
        ('I', 35),
        ('J', 36),
        ('K', 37),
        ('L', 38),
        ('M', 39),
        ('N', 40),
        ('O', 41),
        ('P', 42),
        ('Q', 43),
        ('R', 44),
        ('S', 45),
        ('T', 46),
        ('U', 47),
        ('V', 48),
        ('W', 49),
        ('X', 50),
        ('Y', 51),
        ('Z', 52),
    ]);

    first_task(&contents, &map);
    second_task(&contents, &map);
}
