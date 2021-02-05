routes = []
def find_paths(node, cities, path, distance):
    path.append(node)

    
    if len(path) > 1:
        distance += cities[path[-2]][node]

    
    if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print (path, distance)
        routes.append([distance, path])
        return

   
    for city in cities:
        if (city not in path) and (node in cities[city]):
            find_paths(city, dict(cities), list(path), distance)


if __name__ == '__main__':
    cities = {
        'A': {'B': 5, 'C': 5, 'D': 4, 'E': 3},
        'B': {'A': 5, 'C': 6, 'D': 7, 'E': 1},
        'C': {'A': 5, 'B': 6, 'D': 2, 'E': 4},
        'D': {'A': 4, 'B': 7, 'C': 2, 'E': 6},
        'E': {'A': 3, 'B': 1, 'C': 4, 'D': 6}
    }

    print ("Start: A")
    find_paths('A', cities, [], 0)
    print ("\n")
    routes.sort()
    if len(routes) != 0:
        print ("Shortest route: %s" % routes[0])
    else:
        print ("FAIL!")