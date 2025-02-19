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

struct SolverState {
    vector<Clause> clauses;
    unordered_map<int, int> assignments;  // 1 (true), 0 (false)
    vector<int> decision_stack;  // tracking decisions
    int decision_level = 0;

    //for non-chronological backtracking
    unordered_map<int, Clause*> antecedents; //track assignments
};

bool unit_propagation(SolverState &state, int &conflict_variable) {
    stack<int> propagation_stack; 
    unordered_set<int> visited;

    // Add assigned variables to check for conflicts with the new assignemnt
    for (auto &[var, val] : state.assignments)
        propagation_stack.push(var * (val ? 1 : -1)); //adding polarity as well

    while (!propagation_stack.empty()) {
        int lit = propagation_stack.top();
        propagation_stack.pop();
        
        // be gone duplicate checks >:(
        if (visited.find(lit) != visited.end()) continue;
        visited.insert(lit);

        for (auto &clause : state.clauses) {
            int unassigned = 0; // counts # of unassigned vars
            int last_literal = 0; // stores the last seen unassigned literal 
            bool satisfied = false;

            for (int l : clause.literals) {
                if (state.assignments.count(abs(l))) { //every literal that is assigned, check proper assignment
                    if ((l > 0 && state.assignments[l] == 1) || (l < 0 && state.assignments[-l] == 0)) {
                        satisfied = true;
                        break;
                    }
                } else { //unassigned literal 
                    unassigned++;
                    last_literal = l;
                }
            }
            if (satisfied) continue;

            if (unassigned == 1) { //one unassigned literal ==> assign it immediately 
                state.assignments[abs(last_literal)] = (last_literal > 0) ? 1 : 0;
                propagation_stack.push(last_literal);
            } else if (unassigned == 0) { //unsatisfiable & no more unassigned literals 
                conflict_variable = last_literal;
                return false;
            }
        }
    }
    return true;
}

// Backtrack to the specified decision level
void backtrack(SolverState &state, int level) {
    while (!state.decision_stack.empty() && state.decision_stack.back() > level) {
        int var = abs(state.decision_stack.back());
        state.assignments.erase(var);
        state.antecedents.erase(var);
        state.decision_stack.pop_back();
    }
    state.decision_level = level;
}

// Conflict Analysis s.t. we learn a new clause
Clause conflict_analysis(SolverState &state, int conflict_variable, int &backtrack_level) {
    
    Clause learned_clause; 
    unordered_set<int> seen;
    vector<int> conflict_literals; //storing literals for the learned clause

    //traversing the implication graph
    stack<int> analysis_stack; //conflict variable & back
    //start with variable that caused the issue
    analysis_stack.push(conflict_variable);

    while(!analysis_stack.empty()){
        int var = analysis_stack.top();
        analysis_stack.pop();

        //dont process a processed variable 
        if(seen.count(var)) continue;
        seen.insert(var);

        //does variable have antecedent clause?
        if(state.antecedents.count(var)){
            
            //antecedent == reason it was assigned 
            Clause *reason = state.antecedents[var];
            for(int lit : reason->literals){
                if(lit != var) analysis_stack.push(abs(lit));
            }
        }
        // if no antecedent (no reason for assignment) == decision variable
        else {
            conflict_literals.push_back(-var);
        }
    }

    //which decision levels are involved in conflict 
    backtrack_level = 0;
    for(int lit : conflict_literals) {
        int level = state.assignments[abs(lit)];
        if( level < state.decision_level){
            backtrack_level = max(backtrack_level, level);
        }
    }

    learned_clause.literals = conflict_literals;
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

    while (true) {
        int conflict_variable = 0;
        
        if (!unit_propagation(state, conflict_variable)) {
            if (state.decision_level == 0) return false;  // Conflict at level 0 UNSAT :(
            
            int backtrack_level = 0;
            Clause learned_clause = conflict_analysis(state, conflict_variable, backtrack_level);
            state.clauses.push_back(learned_clause);
            backtrack(state, backtrack_level); // simplified, chronological 

        } else {

            int var = pick_branching_variable(state);
            if (var == -1) return true;  // No conflict & no unassigned variables
            
            // Make a decision == assign True
            state.assignments[var] = 1;
            state.decision_stack.push_back(var);
            state.decision_level++;
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
        /*for (const auto &assignment : state.assignments) {
            cout << assignment.first << " = " << assignment.second << "\n";
        }*/
    } else {
        cout << "UNSATISFIABLE :( \n";
    }
    
    return 0;
}
