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


def get_total_execution_time(graph, total_workers, delay_per_letter):
    available_workers = total_workers
    total_time = -1
    available_keys = []
    ongoing_work = []
    hold_keys = []

    for key in graph:
        if is_available(key, graph):
            available_keys.append(key)

    while len(ongoing_work) != 0 or len(available_keys) != 0 or len(hold_keys) != 0:
        # tick
        total_time += 1

        # update remaining time and check finished works
        for work in list(ongoing_work):
            work['time_left'] -= 1
            if work['time_left'] == 0:
                ongoing_work.remove(work)
                available_workers += 1
                if work['letter'] in graph:
                    del graph[work['letter']]

        if available_workers == 0:
            continue

        for key in hold_keys:
            if is_available(key, graph):
                available_keys.append(key)
        hold_keys = [x for x in hold_keys if x not in available_keys]
        available_keys.sort(reverse=True)

        if len(available_keys) == 0:
            continue

        # get more work
        while available_workers > 0 and len(available_keys) > 0:
            item = available_keys.pop()
            available_workers -= 1
            ongoing_work.append({'time_left': (ord(item) - 64 + delay_per_letter), 'letter': item})
            if item not in graph:
                continue
            items_list = graph[item]

            for next_item in items_list:
                if next_item not in hold_keys:
                    hold_keys.append(next_item)

    return total_time


if __name__ == '__main__':
    graph = parse_input_graph()
    total_time = get_total_execution_time(graph, 5, 60)

    print(total_time)
