#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isBalanced(string expression){
    stack <char> s;

    for(int i = 0; i < expression.length(); i++){
        if(expression[i] == '(' || expression[i] == '{' || expression[i] == '['){
            s.push(expression[i]);
            continue;
        }

        if(s.empty())
            return false;
        
        char c = s.top();

        switch(expression[i]){
            case ')':
                if(c != '(')
                    return false;
    
                break;

            case '}':
                if(c != '{')
                    return false;

                break;
            
            case ']':
                if(c != '[')
                    return false;

                break;
            
            default:
                break;
        }

        s.pop();
    }

    return s.empty();
}

int main(){
    string s = "()()()()()()()";

    if(isBalanced(s))
        cout << "Parentheses are balanced\n";
    else
        cout << "parentheses are not balanced\n";

    return 0;
}