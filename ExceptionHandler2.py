# Program to process exceptions using functions

def main():
    total_score = 0.0
    scores_str = input("Enter numbers separated by spaces: ")
    scores_list = scores_str.split()
    print (scores_list)
    try:
        total_score = computeTotal(scores_list)
        print (total_score)
    except ValueError:
        print("Enter numeric values.")
    except Exception as ex:
        print ("Some error occurred")
        print(type(ex))
        print (ex, "error, specifically.")
    else:
        print ("I'm in main")
        print ("Everything looks good")
        print ("I'm in the else of the main function")
        print ("Total Score:", total_score)
    finally:
        print ("I'm in main")
        print ("Finally, I'm here no matter what")

def computeTotal(scores_list):
    total_score = 0.0
    try:
        i = 0
        while (i < len(scores_list)):
            total_score += int(scores_list[i])
            i += 1
    except ValueError:
        print ("I'm in computeTotal function")
        print ("Enter numeric values")
    else:
        print ("I'm in the else of computeTotal")
        return total_score
# Call main
main()
