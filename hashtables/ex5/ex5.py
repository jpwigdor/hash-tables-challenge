def finder(files, queries):
    paths_by_filename = {}

    for path in files:
        # this just grabs the last word in the split. grabbing just the `filename` from the `filepath query`
        filename = path.split('/')[-1]
        if filename not in paths_by_filename:
            paths_by_filename[filename] = [path]
        else:
            paths_by_filename[filename].append(path)

    result = []

    for query in queries:
        if query in paths_by_filename:
            for path in paths_by_filename[query]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
