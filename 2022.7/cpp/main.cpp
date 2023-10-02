#include <algorithm>
#include <iostream>
#include <map>
#include <memory>
#include <vector>
#include <numeric>
#include <fstream>

using namespace std;

class Directory {
  public:
    shared_ptr<Directory> parent;
    vector<shared_ptr<Directory>> children;
    vector<int> files;
    string name;
    int size;

    Directory(string name_, shared_ptr<Directory> parent_ = nullptr,
              int size_ = 0) {
        this->name = move(name_);
        this->parent = parent_;
        this->size = size_;
    }
};

static map<Directory *, int> MEMO = {};

int getDirectorySize(Directory &directory) {
    if (MEMO.find(&directory) != MEMO.end()) {
        return MEMO.at(&directory);
    }
    int size = 0;
    for (auto file : directory.files) {
        size += file;
    }
    for (auto &child : directory.children) {
        size += getDirectorySize(*child);
    }
    MEMO.insert({&directory, size});
    return size;
}

void first_task(const vector<string> &commands) {
    auto curr_dir = make_shared<Directory>("/");

    for (auto &line : commands) {
        if (line == "$ ls") {
            continue;
        }
        if (line.find("$ cd") != string::npos) {
            string_view target =
                string_view(line.c_str(), line.size()).substr(5);
            if (target == "..") {
                curr_dir = curr_dir->parent;
            } else {
                curr_dir = *std::find_if(
                    begin(curr_dir->children), end(curr_dir->children),
                    [target](auto val) { return val->name == target; });
            }
        } else if (line.find("dir") != string::npos) {
            string_view target =
                string_view(line.c_str(), line.size()).substr(4);
            curr_dir->children.emplace_back(
                make_shared<Directory>(string(target), curr_dir));
        } else if (std::isdigit(line[0])) {
            string_view line_view =
                string_view(line.c_str(), line.size()).substr();
            string_view size_view = line_view.substr(0, line_view.find(' '));
            curr_dir->files.emplace_back(std::stoi(size_view.data()));
        }
    }

    while (curr_dir->parent) {
        curr_dir = curr_dir->parent;
    }

    curr_dir->size = getDirectorySize(*curr_dir);
    std::vector<int> MEMO_values;
    for(auto &item: MEMO){
        if(item.second <= 100000)
            MEMO_values.emplace_back(item.second);
    }
    cout << "First task: " << std::accumulate(begin(MEMO_values), end(MEMO_values), 0) << '\n';
}

void second_task(const vector<string> &commands) {
    auto curr_dir = make_shared<Directory>("/");

    for (auto &line : commands) {
        if (line == "$ ls") {
            continue;
        }
        if (line.find("$ cd") != string::npos) {
            string_view target =
                string_view(line.c_str(), line.size()).substr(5);
            if (target == "..") {
                curr_dir = curr_dir->parent;
            } else {
                curr_dir = *std::find_if(
                    begin(curr_dir->children), end(curr_dir->children),
                    [target](auto val) { return val->name == target; });
            }
        } else if (line.find("dir") != string::npos) {
            string_view target =
                string_view(line.c_str(), line.size()).substr(4);
            curr_dir->children.emplace_back(
                make_shared<Directory>(string(target), curr_dir));
        } else if (std::isdigit(line[0])) {
            string_view line_view =
                string_view(line.c_str(), line.size()).substr();
            string_view size_view = line_view.substr(0, line_view.find(' '));
            curr_dir->files.emplace_back(std::stoi(size_view.data()));
        }
    }

    while (curr_dir->parent) {
        curr_dir = curr_dir->parent;
    }

    curr_dir->size = getDirectorySize(*curr_dir);
    int needed = 30000000 - (70000000 - curr_dir->size);
    int found_min = INT32_MAX;
    auto child = curr_dir;

    for (auto &items : MEMO) {
        if (items.second >= needed) {
            found_min = std::min(found_min, items.second);
        }
    }
    cout << "Second task: " << found_min << '\n';
}

int main(int argc, char *argv[]) {
    ifstream input_file("../input.txt");
    string line;
    vector<string> commands;
    if(!input_file.is_open()){
        cerr << "Couldn't open file\n";
        return 1;
    }
    while(std::getline(input_file, line)){
        commands.emplace_back(move(line));
    }

    first_task(commands);
    second_task(commands);
}