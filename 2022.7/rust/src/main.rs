// use std::collections::HashMap;

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(PartialEq, Eq, Debug)]
struct Directory {
    name: String,
    parent: Option<Rc<Directory>>,
    children: RefCell<Vec<Rc<Directory>>>,
    files: RefCell<Vec<i32>>,
}

fn get_directory_size(directory: Rc<Directory>, memo: &mut HashMap<String, i32>) -> i32 {
    let mut key = String::from(&directory.name);
    let mut parent = directory.parent.clone();
    while parent.is_some() {
        let p = parent.clone().unwrap();
        key += &p.name;
        parent = p.parent.clone();
    }

    if memo.contains_key(&key) {
        return *memo.get(&key).unwrap();
    }
    let mut size = 0;
    for file in directory.files.borrow().clone().into_iter() {
        size += file;
    }
    for child in directory.children.borrow().clone().into_iter() {
        size += get_directory_size(child, memo);
    }
    memo.insert(key, size);
    size
}

fn first_task(commands: &[&str]) {
    let root = Rc::new(Directory {
        name: "/".to_string(),
        parent: None,
        children: RefCell::new(vec![]),
        files: RefCell::new(vec![]),
    });
    let mut curr_dir = root.clone();

    for command in commands {
        if *command == "$ ls" {
            continue;
        }
        {
            let target = command.strip_prefix("$ cd").unwrap_or("").trim();
            if !target.is_empty() {
                if target == ".." {
                    curr_dir = curr_dir.clone().parent.clone().unwrap();
                } else {
                    let mut found: Option<Rc<Directory>> = None;
                    {
                        let children = curr_dir.children.borrow_mut();
                        for child in children.clone().into_iter() {
                            if child.name == target {
                                found = Some(child.clone());
                                break;
                            }
                        }
                    }
                    curr_dir = found.unwrap().clone();
                }
                continue;
            }
        }
        {
            let target = command.strip_prefix("dir").unwrap_or("").trim();
            if !target.is_empty() {
                let child = Rc::new({
                    Directory {
                        name: target.to_string(),
                        parent: Some(curr_dir.clone()),
                        children: RefCell::new(vec![]),
                        files: RefCell::new(vec![]),
                    }
                });
                curr_dir.children.borrow_mut().push(child.clone());
                continue;
            }
        }

        if command[0..1].parse::<i32>().is_ok() {
            let size_str = command.split(' ').next().unwrap();
            let size = size_str.parse::<i32>().unwrap();
            curr_dir.files.borrow_mut().push(size);
        }
    }

    let mut memo: HashMap<String, i32> = HashMap::new();
    let _ = get_directory_size(root.clone(), &mut memo);
    let mut result = 0;
    for item in memo.into_iter() {
        if item.1 <= 100000 {
            result += item.1;
        }
    }
    println!("first_task: {}", result);
}

fn second_task(commands: &[&str]) {
    let root = Rc::new(Directory {
        name: "/".to_string(),
        parent: None,
        children: RefCell::new(vec![]),
        files: RefCell::new(vec![]),
    });
    let mut curr_dir = root.clone();

    for command in commands {
        if *command == "$ ls" {
            continue;
        }
        {
            let target = command.strip_prefix("$ cd").unwrap_or("").trim();
            if !target.is_empty() {
                if target == ".." {
                    curr_dir = curr_dir.clone().parent.clone().unwrap();
                } else {
                    let mut found: Option<Rc<Directory>> = None;
                    {
                        let children = curr_dir.children.borrow_mut();
                        for child in children.clone().into_iter() {
                            if child.name == target {
                                found = Some(child.clone());
                                break;
                            }
                        }
                    }
                    curr_dir = found.unwrap().clone();
                }
                continue;
            }
        }
        {
            let target = command.strip_prefix("dir").unwrap_or("").trim();
            if !target.is_empty() {
                let child = Rc::new({
                    Directory {
                        name: target.to_string(),
                        parent: Some(curr_dir.clone()),
                        children: RefCell::new(vec![]),
                        files: RefCell::new(vec![]),
                    }
                });
                curr_dir.children.borrow_mut().push(child.clone());
                continue;
            }
        }

        if command[0..1].parse::<i32>().is_ok() {
            let size_str = command.split(' ').next().unwrap();
            let size = size_str.parse::<i32>().unwrap();
            curr_dir.files.borrow_mut().push(size);
        }
    }

    let mut memo: HashMap<String, i32> = HashMap::new();
    let root_size = get_directory_size(root, &mut memo);
    let needed = 30000000 - (70000000 - root_size);
    let mut found_min = i32::MAX;

    for val in memo.values() {
        if *val >= needed {
            found_min = i32::min(found_min, *val)
        }
    }

    println!("second task: {}", found_min);
}

fn main() {
    let input_file = std::fs::read_to_string("./input.txt").unwrap();
    let commands: Vec<&str> = input_file.lines().collect();
    first_task(&commands);
    second_task(&commands);
}
