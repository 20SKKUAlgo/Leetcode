#include <iostream>
#include <string>
#include <stack>


class MinStack {

    int min=0;
    stack<int> s;
    stack<int> m;

public:
    MinStack() {
        min=0;
    }
    
    void push(int val) {
        s.push(val);
        
        if(m.empty()){ // m이 비어있을때
            m.push(val);

        }
        else if(m.top()>=val){ // val이 최소값일때
            m.push(val);
        }
        else{
            int t = m.top();
            m.push(t);
        }
    }
    
    void pop() {
        s.pop();
        m.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return m.top();
    }
};
