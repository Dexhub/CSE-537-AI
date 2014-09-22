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
  
  #print "Start:", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  #print "Start's successors:", problem.getSuccessors(problem.getStartState())
  visitedlist = []
  "*** YOUR CODE HERE ***"
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
      print value[1]
      if value[1] == 'South':
        outputlist.append(s)
      elif value[1] == 'North':
        outputlist.append(n)
      elif value[1] == 'East':
        outputlist.append(e)
      elif value[1] == 'West':
        outputlist.append(w)
      
  #print str(outputlist[::-1])
  return outputlist[::-1]
    
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  from game import Directions
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
  util.raiseNotDefined()
  
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
  print "Current state is " + str(currentPosition)
  #if not type(currentPosition) is tuple:
  #  for value in currentState:
  #    if type(value) is tuple:
  #      currentPosition = value
  #      break
  #print type(currentPosition[2])     
  #for value in currentPosition:
  #  print type(value)
  #print str(currentPosition)
  
  for successor in problem.getSuccessors(currentPosition):
    successorPosition = successor[0]
    
    if not successorPosition in visitedlist:
      if(problem.isGoalState(successorPosition)):
        stack.push(successor)
        print "Pushed " + str(successor) + "in stack"
        print "Goal Achieved"
        return 1
      stack.push(successor)
      visitedlist.append(successorPosition)
      print "Pushed " + str(successor) + "in stack"
      if recurseDFS(stack, problem, visitedlist) == 1:
        return 1	
  stack.pop()  
    #print "Current stack is " + str(stack)
  return 0
  #util.raiseNotDefined()

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
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch