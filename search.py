# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  from game import Directions
  from util import Stack, Queue
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST

  visitedlist = []
  "*** YOUR CODE HERE ***"
  qu = Queue()
  st = Stack()
  outputlist = []
  st.push({'child':problem.getStartState(),'parent':None})
  qu.push(problem.getStartState())
  visitedlist.append(problem.getStartState())
  pa = None
  if recurseBFS(qu,st,problem,visitedlist) == 0:
    print "No Path exists"
  else:
    flag = 1
    while not st.isEmpty():
      value = st.pop()
      #print "parent -" + str(value['parent']) + " ch-"+ str(value['child']) +"pa -"+ str(pa)
      if not value['parent'] or value['child'] == pa or flag == 1:
        flag = 0
        ch , pa = value['child'], value['parent']
        if value['child'][1] == 'South':
          outputlist.append(s)
        elif value['child'][1] == 'North':
          outputlist.append(n)
        elif value['child'][1] == 'East':
          outputlist.append(e)
        elif value['child'][1] == 'West':
          outputlist.append(w)

  #print str(outputlist[::-1])
  return outputlist[::-1]

def recurseBFS(queue, stack, problem,visitedlist):
  "Find out the path by popping out elements from stack one by one, filling successors in it."
  "Instert successors only when they are not visited"
  "Maintain a variable visitedlist to check the states visited"
  "*** YOUR CODE HERE ***"
  currentState = queue.pop()
  if len(currentState) == 2:
    currentPosition = currentState
  else:
    currentPosition = currentState[0]
  #print "Current state is " + str(currentPosition)


  for successor in problem.getSuccessors(currentPosition):
    successorPosition = successor[0]
    if not successorPosition in visitedlist:
      if(problem.isGoalState(successorPosition)):
        stack.push({'child':successor,'parent':currentState})
        queue.push(successor)
        #print "Pushed " + str(successor) + "in stack"
        print "Goal Achieved"
        return 1
      stack.push({'child':successor,'parent':currentState})
      queue.push(successor)
      visitedlist.append(successorPosition)
      #print "Pushed " + str(successor) + "in stack"
  if recurseBFS(queue, stack, problem, visitedlist) == 1:
    return 1
  #print "Current stack is " + str(stack)
  return 0
  #util.raiseNotDefined() 
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"

  from game import Directions
  from util import PriorityQueue
  from searchAgents import manhattanHeuristic;
  import collections;
  open_pq = PriorityQueue();

  start = None;
  if hasattr(problem, 'startState'):
    start = problem.startState;
  else:
    start = problem.start;

  # nodes map is used to store the information about nodes class for each state that we expand.
  # Definition of node class can be found after this method
  nodes = {};

  # this list stores the state of all the nodes that we are traversing
  closed_list = [];

  # creating node object of the start state and pushing it into priority queue with value 0
  node = Node(None, start);
  open_pq.push(node.state, 0);
  nodes[node.state] = node;

  while not (open_pq.isEmpty()):

    # Popping node with smallest cost from priority queue
    cur_state  = open_pq.pop();
    cur_node = nodes[cur_state];

    # Append current state to closed list as we are expanding it
    closed_list.append(cur_state);

    # check if current state is the goal state
    if problem.isGoalState(cur_state):
      # if yes then traverse from goal to startState using parent attribute of Node class
      direction_rev = []
      prev = cur_state;
      while prev != start:
        direction_rev.append(nodes[prev].direction);
        prev = nodes[prev].parent;
      direction_rev.append(nodes[prev].direction);

      # This will give us path from start to end in reverse order. We simply reverse the list again
      directions = []
      for item in reversed(direction_rev):
        if item is not None:
          directions.append(item);

      return directions;

    # Get the successors of the current node
    successors = problem.getSuccessors(cur_state);

    # For every item in successor, we check if its in closed list. If it's not then we add it after calculating
    # f value, Node creation and pushing it into priority queue.
    for item in successors:
      if item[0] not in closed_list:
        g = cur_node.g + heuristic(cur_state, problem);
        h = heuristic(item[0], problem);
        f = g + h;
        child = Node(cur_state, item[0], f, g, h, item[1]);
        nodes[child.state] = child;
        open_pq.push(item[0], f);

# Node class to hold different values of state
class Node(object):

  def __init__(self, parent = None, state = None, f = 0, g = 0, h = 0, direction = None):
    self.parent = parent;
    self.state = state;
    self.f = f;
    self.g = g;
    self.h = h;
    self.direction = direction;

  def getState(self):
    return self.state;

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch