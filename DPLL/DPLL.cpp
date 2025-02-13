#include <iostream> 
#include <fstream>
#include <sstream>

#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <optional>
using namespace std;

//CNF Formula Structure 
using Clause = vector<int>;
using Formula = vector<Clause>;

void simplify(Formula &formula, int literal){
    Formula simplified;

    for (const auto &clause : formula) {
        //if the clause contains the literal, skip it
        if (find(clause.begin(), clause.end(), literal) != clause.end())
            continue;

        Clause newClause;
        for (int lit : clause) {
            //ignore the negation of the literal, add the rest
            if (lit != -literal) newClause.push_back(lit);
        }

        //if we ignored all the literals in clause, unsatsifable
        if (newClause.empty()){
            formula = {{}};
            return;
        }
        
        simplified.push_back(newClause);
    }
    formula = move(simplified);
}

optional<int> findUnitClause(const Formula &formula){
    for (const auto &clause : formula) {
        // returns the first literal if singleton 
        if (clause.size() == 1) 
            return clause[0];         
    }

    return nullopt;
}

void pureLiteralElimination(Formula &formula, unordered_set<int> & assignments){
    unordered_map<int, int> literalCount;
    unordered_set<int> pureLiterals;

    //counting the number of every literal
    for(const auto &clause : formula){
        for(int literal : clause){
            literalCount[literal]++;
        }
    }

    //Does it exist in the other polarity? if no then pure 
    for(const auto & literal : literalCount){
        if(!literalCount.count(-literal.first)){
            pureLiterals.insert(literal.first);
        }
    }

    //Assign what satisfies the clause & simplify 
    for(const auto &literal : pureLiterals){
        assignments.insert(literal);
        simplify(formula, literal);
    }
}

bool dpll(Formula formula, unordered_set<int> &assignments) {
    if(formula.empty()) return true;

    for (const auto &clause : formula)
        if (clause.empty()) return false;

    //Unit Propagation (single literal clause)
    auto unit = findUnitClause(formula);
    while (unit) {
        int literal = *unit;
        assignments.insert(literal);
        simplify(formula, literal);
        unit = findUnitClause(formula);
    }
    if(formula.empty()) return true;

    //Pure Literal Elimination (no polarity)
    pureLiteralElimination(formula, assignments);
    if (formula.empty()) return true;

    //Make a decision, pick first literal of first clause 
    int chosenLiteral = formula[0][0];
    Formula simplifiedFormula = formula;
    simplify(simplifiedFormula, chosenLiteral);
    assignments.insert(chosenLiteral);

    //Test if the assignment leads to a SAT CNF else erase
    if (dpll(simplifiedFormula, assignments)) return true;
    assignments.erase(chosenLiteral);

    //Test its negation
    simplifiedFormula = formula; 
    simplify(simplifiedFormula, -chosenLiteral);
    assignments.insert(-chosenLiteral);

    if (dpll(simplifiedFormula, assignments)) return true;
    assignments.erase(-chosenLiteral);

    //If neither polarity makes it SAT, it is UNSAT 
    return false; 
}

//PARSE >:) DIMACS format 
Formula read_cnf(const string &filename){
    Formula formula;
    ifstream file(filename);
    string line;

    while(getline(file, line)){
        if(line.empty() || line[0] == 'c' || line[0] == 'p') continue;
        Clause clause;
        int literal;
        stringstream ss(line);
        while (ss >> literal && literal != 0) {
            clause.push_back(literal);
        }
        formula.push_back(clause);
    }

    return formula; 

}

int main() {
    Formula formula = read_cnf("");
    unordered_set<int> assignments;

    if(dpll(formula, assignments)) {
        cout << "SATISFIABLE <3\n";
        //cout << "Satisfiable <3\nAssignments:";
        /*for(int literal : assignments) {
            cout << literal << " ";
        }
        cout << endl;*/
    }
    else {
        cout << "UNSATISFIABLE :(\n";
    }

    return 0;
}
