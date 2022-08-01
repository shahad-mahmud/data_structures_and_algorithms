#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector <vector<int>> graph;
vector <bool> flag;

void connect_edge(int from, int to){
    graph[from].push_back(to);
}

void bfs(int start_node){
    queue <int> q;

    q.push(start_node); // add the start node to start visit
    flag[start_node] = true; // mark the fast node as visited

    while(!q.empty()){
        int front_node = q.front();
        q.pop(); // remove the top node

        cout<< front_node << endl;

        // add all adjacent nodes to the queue
        for(vector<int> :: iterator i = graph[front_node].begin(); i != graph[front_node].end(); i++){
            if(!flag[*i]){
                q.push(*i);
                flag[*i] = true; // mark it as visited
            }
        }
    }
}

int main(){
    int nodes = 4;

    flag.assign(nodes, false);
    graph.assign(nodes, vector<int>());

    connect_edge(0,1);
    connect_edge(0,2);
    connect_edge(1,2);
    connect_edge(2,1);
    connect_edge(3,2);
    connect_edge(2,3);

    bfs(0);

    return 0;
}