import re
if __name__ == '__main__':
    T = [0,0,0,0,0]
    R = [0,0,0,0,0]
    T[0] = "test1a"
    R[0] = "Wrong answer"
    T[1] = "test2"
    R[1] = "OK"
    T[2] = "test1b"
    R[2] = "Runtime error"
    T[3] = "test1c"
    R[3] = "OK"
    T[4] = "test3"
    R[4] = "Time limit exceeded"

    results = dict()
    for test, result in zip(T, R):
        print test, result

        match = re.match(r"([a-z]+[0-9]+)([a-z]+)", test, re.I)
        if match:
            items = match.groups()
            test_group = items[0]
            test_sequence = items[1]
        else:
            test_group = test
            test_sequence = None

        if test_group not in results:
            if result == "OK":
                results[test_group] = 1
            else:
                results[test_group] = 0
        else:
            if results.get(test_group) == 1 and result != "OK":
                results[test_group] = 0

    passed = 0
    for value in results.values():
        if value == 1:
            passed += 1


    print int(passed * 100 / len(results))