import sys


def parse_input_graph():
    graph = {}

    with open('input.txt') as f:
        for line in f:
            words = line.split(' ')
            source = words[1]
            destination = words[7]

            if source in graph:
                graph[source].append(destination)
            else:
                graph[source] = [destination]

    return graph


def is_available(key, graph):
    for k, value in graph.items():
        if key in value:
            return False

    return True


def order_flow(graph):
    result = []
    available_keys = []
    hold_keys = []

    for key in graph:
        if is_available(key, graph):
            available_keys.append(key)

    while len(available_keys) != 0 or len(hold_keys) != 0:
        for key in hold_keys:
            if is_available(key, graph):
                available_keys.append(key)
        hold_keys = [x for x in hold_keys if x not in available_keys]
        available_keys.sort(reverse=True)

        item = available_keys.pop()
        if item not in graph:
            result.append(item)
            continue
        items_list = graph[item]

        del graph[item]

        for next_item in items_list:
            if next_item not in hold_keys:
                hold_keys.append(next_item)

        result.append(item)

    return result


if __name__ == '__main__':
    graph = parse_input_graph()
    result = order_flow(graph)

    for c in result:
        sys.stdout.write(c)

    sys.stdout.write('\n')
