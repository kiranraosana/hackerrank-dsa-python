if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    avg_scores = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        avg_scores.append(sum(scores)/len(scores))
        student_marks[name] = scores
    query_name = input()
    
    for i, j in student_marks.items():
        avg = '{0:.2f}'.format(sum(j)/len(j))
        student_marks[i] = avg
    
    
    print(student_marks[query_name])