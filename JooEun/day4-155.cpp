// 2023.01.05 https://leetcode.com/problems/min-stack/

// #include <algorithm>
// #include <vector>

class MinStack {
public:
    vector<int> stack; // member variable
    
    MinStack() {
      // default constructor
    }
    
    void push(int val) {
        stack.push_back(val);
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        // https://notepad96.tistory.com/40 :: use algorithm library
        return *min_element(stack.begin(), stack.end());
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
