#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <algorithm>

using namespace std;

struct Clause {
    vector<int> literals;
};

struct AssignmentInfo {
    int value;      // 1 for true, 0 for false
    int level;      
    Clause *reason;     
};

struct SolverState {
    vector<Clause> clauses;
    unordered_map<int, AssignmentInfo> assignments;  
    vector<int> trail; 
    int decision_level = 0;
};

bool unit_propagation(SolverState &state, Clause &conflict_clause) {
    bool progress = true;

    while (progress) {
        progress = false; 
        
        for (auto &clause : state.clauses) {
            int unassigned = 0; // counts # of unassigned vars
            int last_literal = 0; // stores the last seen unassigned literal 
            bool satisfied = false;

            for (int l : clause.literals) {
                int var = abs(l);
                auto it = state.assignments.find(var);
                if (it != state.assignments.end()) { 
                    int val = it->second.value;
                    if ((l > 0 && val == 1) || (l < 0 && val == 0)) {
                        satisfied = true;
                        break;
                    }
                } else { //unassigned literal 
                    unassigned++;
                    last_literal = l;
                }
            }
            if (satisfied) continue;

            if (unassigned == 0) {
                conflict_clause = clause;
                return false;
            }

            if (unassigned == 1) { //one unassigned literal ==> assign it immediately 
                int var = abs(last_literal);
                int val = (last_literal > 0) ? 1 : 0;

                if(state.assignments.find(var) == state.assignments.end()){
                    AssignmentInfo info;
                    info.value = val;
                    info.level = state.decision_level;
                    info.reason = &clause;
                    state.assignments[var] = info;
                    state.trail.push_back(var);
                    progress = true;
                }
            }        
        }
    }
    return true;
}

// Backtrack to the specified decision level
void backtrack(SolverState &state, int level) {
    while (!state.trail.empty()) {
        int var = state.trail.back();
        if (state.assignments[var].level > level){
            state.assignments.erase(var);
            state.trail.pop_back();
        }
    }
    state.decision_level = level;
}

// Conflict Analysis s.t. we learn a new clause
Clause conflict_analysis(SolverState &state, Clause &conflict_clause, int &backtrack_level) {
    // Start with the conflict clause.
    Clause learned_clause = conflict_clause;
    int current_level = state.decision_level;
    
    // Count the number of literals in learned_clause assigned at the current decision level.
    int count = 0;
    for (int lit : learned_clause.literals) {
        int var = abs(lit);
        if (state.assignments[var].level == current_level)
            count++;
    }
    
    int i = state.trail.size() - 1;
    while (count > 1 && i >= 0) {
        int var = state.trail[i];
        bool inClause = false;
        for (int lit : learned_clause.literals) {
            if (abs(lit) == var && state.assignments[var].level == current_level) {
                inClause = true;
                break;
            }
        }
        if (!inClause) {
            i--;
            continue;
        }
        
        Clause *reason = state.assignments[var].reason;
        if (reason == nullptr) {
            i--;
            continue;
        }
        
        vector<int> new_literals;
        for (int lit : learned_clause.literals) {
            if (abs(lit) == var) continue;
            new_literals.push_back(lit);
        }
        for (int lit : reason->literals) {
            if (abs(lit) == var) continue;
            bool duplicate = false;
            for (int existing : new_literals) {
                if (existing == lit) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate)
                new_literals.push_back(lit);
        }
        learned_clause.literals = new_literals;
        
        count = 0;
        for (int lit : learned_clause.literals) {
            int v = abs(lit);
            if (state.assignments[v].level == current_level)
                count++;
        }
        i--;
    }
    
    backtrack_level = 0;
    for (int lit : learned_clause.literals) {
        int var = abs(lit);
        int lvl = state.assignments[var].level;
        if (lvl != current_level && lvl >= backtrack_level)
            backtrack_level = lvl;
    }
    
    return learned_clause;
}


// Heuristic : pick most frequent unassigned !! 
int pick_branching_variable(const SolverState &state) {
    unordered_map<int, int> occurrence_count;
    
    for (const auto &clause : state.clauses) {
        for (int lit : clause.literals) {
            if (state.assignments.find(abs(lit)) == state.assignments.end()) {
                occurrence_count[abs(lit)]++;
            }
        }
    }
    
    //max frequency
    int best_var = -1, max_count = -1;
    for (const auto &[var, count] : occurrence_count) {
        if (count > max_count) {
            best_var = var;
            max_count = count;
        }
    }
    
    return best_var;
}

bool cdcl_solve(SolverState &state) {
    if(state.clauses.empty()) return true;

    for (const auto &clause : state.clauses){
        if (clause.literals.empty()) return false;
    } 
    Clause conflict_clause;
    while (true) {
    
        if (!unit_propagation(state, conflict_clause)) {
            if (state.decision_level == 0) return false;  // Conflict at level 0 UNSAT :(
            
            int backtrack_level = 0;
            Clause learned_clause = conflict_analysis(state, conflict_clause, backtrack_level);
            //if(state.clauses.find(learned_clause) == state.clauses.end())
            state.clauses.push_back(learned_clause);
            backtrack(state, backtrack_level); 

        } else {

            int var = pick_branching_variable(state);
            if (var == -1) return true;  
            state.decision_level++;
            AssignmentInfo info;
            info.value = 1;  
            info.level = state.decision_level;
            info.reason = nullptr; 
            state.assignments[var] = info;
            state.trail.push_back(var);
        }
    }
}

//PARSE >:) DIMACS format 
vector<Clause> read_cnf(const string &filename){
    vector<Clause> formula;
    ifstream file(filename);
    string line;

    while(getline(file, line)){
        if(line.empty() || line[0] == 'c' || line[0] == 'p') continue;
        Clause clause;
        int literal;
        stringstream ss(line);
        while (ss >> literal && literal != 0) {
            clause.literals.push_back(literal);
        }
        if(!clause.literals.empty())formula.push_back(clause);
    }

    return formula; 

}

int main() {
    SolverState state;
    state.clauses = read_cnf(" ");
   
    if (cdcl_solve(state)) {
        cout << "SATISFIABLE <3 \n";
        for (const auto &assignment : state.assignments) {
            cout << assignment.first << " = " << assignment.second.value << "\n";
        }
    } else {
        cout << "UNSATISFIABLE :( \n";
    }
    
    return 0;
}
