def find_runner_up(scores):
    # Remove duplicates from the list of scores
    unique_scores = list(set(scores))

    # Sort the unique scores in descending order
    unique_scores.sort(reverse=True)

    # Return the second highest score
    return unique_scores[1]


# Example usage:
scores = [2, 3, 6, 6, 5]  # Sample scores
runner_up_score = find_runner_up(scores)
print("The runner-up score is:", runner_up_score)

