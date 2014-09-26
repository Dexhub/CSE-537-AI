#!/bin/sh
echo "#################################################"
echo "Testing DFS"
echo "#################################################"
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent

echo "#################################################"
echo "Testing BFS"
echo "#################################################"
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

echo "#################################################"
echo "Testing UCS"
echo "#################################################"
python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs

echo "#################################################"
echo "Testing A* with heuristic"
echo "#################################################"
python pacman.py -l tinyMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 

echo "#################################################"
echo "Testing A* with heuristic"
echo "#################################################"
python pacman.py -l tinyMaze -z .5 -p SearchAgent -a fn=astar 
python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar 
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar 


echo "#################################################"
echo "Corner Problem"
echo "#################################################"
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem


echo "#################################################"
echo "Corner Problem with A*"
echo "#################################################"
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

echo "#################################################"
echo "A* Food search agent"
echo "#################################################"
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
