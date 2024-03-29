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
from util import Stack, Queue

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

#############################################################################

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  
  visitedlist = []
  st = Stack()
  outputlist = []
  st.push(problem.getStartState())
  visitedlist.append(problem.getStartState())
  recurseDFS(st,problem,visitedlist)
  if st.isEmpty():
    print "No Path exist"
  else:
    while not st.isEmpty():
      value = st.pop()
      if len(value) == 2:
        continue
      if value[1] == 'South':
        outputlist.append(s)
      elif value[1] == 'North':
        outputlist.append(n)
      elif value[1] == 'East':
        outputlist.append(e)
      elif value[1] == 'West':
        outputlist.append(w)
      
  return outputlist[::-1]
    

def recurseDFS(stack, problem,visitedlist):
  "Find out the path by popping out elements from stack one by one, filling successors in it."
  "Instert successors only when they are not visited"
  "Maintain a variable visitedlist to check the states visited"
  "*** YOUR CODE HERE ***"
  currentState = stack.pop()
  stack.push(currentState);
  if len(currentState) == 2:
    currentPosition = currentState
  else:
    currentPosition = currentState[0]
  
  for successor in problem.getSuccessors(currentPosition):
    successorPosition = successor[0]
    
    if not successorPosition in visitedlist:
      if(problem.isGoalState(successorPosition)):
        stack.push(successor)
        return 1
      stack.push(successor)
      visitedlist.append(successorPosition)
      if recurseDFS(stack, problem, visitedlist) == 1:
        return 1	
  stack.pop()  
  return 0

#############################################################################
def breadthFirstSearch(problem):

  open_pq=util.Queue()
  closed_list=[];
  Successors=[]

  open_pq.push((problem.getStartState(),[]))

  while open_pq.isEmpty() is False:
      curr_state, path_till_curr_state=open_pq.pop()

      if problem.isGoalState(curr_state) is True:
        return path_till_curr_state

      if curr_state not in closed_list:
        Successors=problem.getSuccessors(curr_state)
        Successors.reverse()

        for item in Successors:
          if item not in closed_list:
            temp=path_till_curr_state + [item[1]]
            open_pq.push((item[0],temp))

      closed_list.append(curr_state);

#############################################################################
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  from sets import Set
  
  from game import Directions
  from util import PriorityQueue
  from searchAgents import manhattanHeuristic;
  import collections;
  pq = PriorityQueue();
  nodes = {};

  # this list stores the state of all the nodes that we are traversing
  explored = [];

  node = UCSNode(None, problem.startState, count=0)
  pq.push(node.state,0)
  nodes[node.state] = node
  
  if problem.isGoalState(problem.getStartState()):
      return 1 # Check what to return in this case
    
  while not (pq.isEmpty()):
      cur_state = pq.pop()
      cur_node = nodes[cur_state]
      count = nodes[cur_state].count
      explored.append(cur_state)
      
      if(problem.isGoalState(cur_state)):
          # if yes then traverse from goal to startState using parent attribute of UCSNode class
          direction_rev = []
          prev = problem.goal;
          direction_rev.append(nodes[prev].direction);
          while prev != problem.startState:
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

      for item in successors:
          successorPos = item[0]
          successorMov = item[1]
          if successorPos not in explored:
              child = UCSNode(cur_state, item[0], count+1, item[1])
              nodes[child.state] = child
              pq.push(item[0], count + 1)


# UCSNode class to hold different values of state
class UCSNode(object):

  def __init__(self, parent = None, state = None, count = 0, direction = None):
    self.parent = parent;
    self.state = state;
    self.count = count;
    self.direction = direction;

  def getState(self):
    return self.state;

#############################################################################
def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."

  from game import Directions
  from util import PriorityQueue
  from searchAgents import manhattanHeuristic;
  import collections;

  # Create priority queue to push fringe elements
  open_pq = PriorityQueue();

  start = problem.getStartState();

  # this list stores the state of all the nodes that are expanded
  closed_list = [];

  # Push the start state to Priority Queue with value 0, so it can be popped first time.
  open_pq.push((start, 0, []), 0);

  while open_pq.isEmpty() is False:

    # Popping node with smallest cost from priority queue
    curr_state, cost_till_curr_state, path_till_curr_state  = open_pq.pop();

    # check if current state is the goal state. If it is then return the path_till_curr_state. Initially I was
    # backtracking till start state and then return the reverse of this backtracked direction list. By passing path_till_successor
    # every time I was able to avoid that unnecessary computation and make code more cleaner
    if problem.isGoalState(curr_state):
      return path_till_curr_state;

    '''
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
    '''

    # if current state is not in closed list then we get all the successors of the curr_state.
    # For every item in successor, we check if its in closed list. If it's not then we calculate the
    # f = g + h value for it and push it to priority queue.

    if curr_state not in closed_list:
      # Get the successors of the current node
      successors = problem.getSuccessors(curr_state);
      successors.reverse()
      for item in successors:
        if item[0] not in closed_list:
          # h value is manhattan distance between current state to goal
          h = heuristic(item[0], problem);
          # g value is the cost to reach current + cost to reach successor from current state which is 1 in our case
          g = cost_till_curr_state + item[2];
          f = g + h;
          # Add successor to path
          path_till_successor = path_till_curr_state + [item[1]]
          # Push successor state, cost and path till successor to priority queue
          open_pq.push((item[0], g, path_till_successor), f);
    # Append current state to closed list as it's expanded
    closed_list.append(curr_state);

  util.raiseNotDefined()

#############################################################################

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
